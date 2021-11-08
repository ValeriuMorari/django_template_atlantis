from django.contrib import admin
from .models import HilModel, TestCase


@admin.register(HilModel)
class HilModelAdmin(admin.ModelAdmin):
    list_display = ['hil_host', 'type', 'had_architecture']


# admin.site.register(HilModel)
admin.site.register(TestCase)
