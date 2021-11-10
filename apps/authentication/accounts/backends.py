from django.conf import settings
from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .__ldap import check_credentials
UserModel = get_user_model()


class AuthBackend(ModelBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("MYAUTH:USER:{}".format(username))
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            if not user.email:
                user.email = "{}@contiwan.com".format(user)
                user.save()
            print("AUTHUSER:{}".format(user))
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            if check_credentials(username, password) is True:
                print("LDAP successfull authorization")
                user = User.objects.create_user(username=username, password=password)
                user.email = "{}@contiwan.com".format(user)
                user.save()
                return user
            else:
                return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
