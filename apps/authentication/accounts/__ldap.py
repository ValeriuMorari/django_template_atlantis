# Resource of code :https://gist.github.com/ibeex/1288159
import ldap
import logging

LOGGER = logging.getLogger(__name__)


# noinspection PyBroadException
def check_credentials(username, password):
    """
    Verifies credentials for username and password.
    Returns None on success or a string describing the error on failure
    """
    domains = ['cw01', 'auto']
    ldap_server = 'ldap://contiwan.com:3268'
    ldap_password = password
    base_dn = 'DC=contiwan,DC=com'
    ldap_filter = f'(&(sAMAccountName={username}) (objectClass=person))'
    fields = ['title',
              'sn',
              'givenName',
              'co',
              'department',
              'company',
              'streetAddress',
              'employeeID',
              'mail',
              'manager',
              'mobile',
              'global-ExtensionAttribute26']

    scope = ldap.SCOPE_SUBTREE
    attrs = ['memberOf']
    ldap_client = None
    connected = False
    for domain in domains:
        try:
            # build a client
            # fully qualified AD user name
            ldap_username = "{}\\{}".format(domain, username)
            ldap_client = ldap.initialize(ldap_server)
            # perform a synchronous bind
            ldap_client.set_option(ldap.OPT_REFERRALS, 0)
            ldap_client.simple_bind_s(ldap_username, ldap_password)
            details = ldap_client.search_s(base=base_dn, scope=scope, filterstr=ldap_filter, attrlist=fields)
            connected = True
            break
        except ldap.INVALID_CREDENTIALS:
            LOGGER.info('Domain check: {} --> Wrong username or password'.format(domain))
            if ldap_client:
                try:
                    ldap_client.unbind()
                except Exception as error:
                    LOGGER.info("unbind error")

        except ldap.SERVER_DOWN:
            LOGGER.info('AD server not available')
            return False

    try:
        ldap_client.unbind()
    except Exception as error:
        LOGGER.info("unbind error")
    return connected


if __name__ == "__main__":
    LOGGER.info(check_credentials("uids3119", "19jenkinsSIL"))
