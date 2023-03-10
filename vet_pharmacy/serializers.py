from rest_framework import serializers

from .models import Medicament, Manufacturer, Pharmacy


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'