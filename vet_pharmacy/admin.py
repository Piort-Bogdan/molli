from django.contrib import admin

from .models import Medicament, Manufacturer, Pharmacy


@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    pass
