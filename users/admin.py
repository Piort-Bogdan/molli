from django.contrib import admin

from .models import DoctorProfile, Pet, PetOwnerProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(PetOwnerProfile)
class PetOwnerProfileAdmin(admin.ModelAdmin):
    pass
