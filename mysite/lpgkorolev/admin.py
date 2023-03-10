from django.contrib import admin
from .models import Service, Specialist, Appointment


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('service', 'specialist', 'first_name', 'last_name', 'phone_number', 'fact_date')
    list_display_links = ('service', 'specialist', 'first_name', 'last_name')
    search_fields = ('service', 'specialist', 'first_name', 'last_name')
    # list_editable = ('service', 'specialist', 'first_name', 'last_name')
    list_filter = ('service', 'specialist', 'fact_date')
    fields = ('service', 'specialist', 'first_name', 'last_name', 'phone_number', 'fact_date')
    save_on_top = True


admin.site.register(Service, ServiceAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.site_title = 'Управление записью'
admin.site.site_header = 'Управление записью'