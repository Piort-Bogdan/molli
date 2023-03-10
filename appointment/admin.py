from django.contrib import admin

from .models import Reception, Appointment

@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass
