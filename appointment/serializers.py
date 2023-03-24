from rest_framework import serializers

from .models import Appointment, Reception


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('pet', 'description', 'owner', 'appointment_time', 'appointment_date')

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'

