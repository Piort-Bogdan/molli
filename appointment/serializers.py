from rest_framework import serializers

from .models import Appointment, Reception


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

