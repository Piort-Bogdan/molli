from rest_framework import serializers

from .models import Appointment, Reception
from .utilites.send_pdf import create_word_and_convert_to_pdf


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('pet', 'description', 'owner', 'appointment_time', 'appointment_date')

class ReceptionSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='owner.phone_number', read_only=True)
    species = serializers.CharField(source='pet.species', read_only=True)
    year_of_birth = serializers.CharField(source='pet.year_of_birth', read_only=True)
    class Meta:
        model = Reception
        fields = ('id', 'doctor', 'owner', 'pet', 'price', 'date', 'temperature', 'preliminary_diagnosis',
                  'appointments', 'send_to_email', 'recommended_researches', 'weight', 'gender', 'phone_number',
                  'species', 'year_of_birth', )
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['doctor'] = instance.doctor.name
        data['pet'] = instance.pet.name
        data['owner'] = instance.owner.name
        data['phone_number'] = instance.owner.phone_number
        data['species'] = instance.pet.species
        print(data)
        create_word_and_convert_to_pdf(data)
        return data


