from rest_framework import serializers

from .models import Pet, PetOwnerProfile, DoctorProfile


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetOwnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerProfile
        fields = '__all__'


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'