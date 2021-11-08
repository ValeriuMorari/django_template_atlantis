from django.contrib import admin
from .models import HilModel, TestCase
from simple_history import register
from django.contrib.auth.models import User


@admin.register(HilModel)
class HilModelAdmin(admin.ModelAdmin):
    list_display = ['hil_host', 'type', 'had_architecture']


register(User)
# admin.site.register(HilModel)
admin.site.register(TestCase)
