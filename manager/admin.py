from django.contrib import admin

from .models import Report, Zone


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'created', 'active')
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'notes']
    date_hierarchy = 'created'


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'created', 'active')
    list_filter = ['user__email', 'active', 'created', 'updated']
    search_fields = ['user__email', 'user__first_name', 'name', 'notes']
    date_hierarchy = 'created'
