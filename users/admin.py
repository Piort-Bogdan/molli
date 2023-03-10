from django.contrib import admin

from .models import User, Pet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


