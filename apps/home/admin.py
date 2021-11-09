from django.contrib import admin
from .models import HilModel, TestCase
from simple_history.admin import SimpleHistoryAdmin


@admin.register(HilModel)
class HilModelAdmin(SimpleHistoryAdmin):
    list_display = ['hil_host', 'type', 'had_architecture']


# admin.site.register(HilModel)
admin.site.register(TestCase, SimpleHistoryAdmin)
