from rest_framework import serializers

from users.models import Pet
from .models import Appointment, Reception
from .utilites.send_pdf import create_docx


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('pet', 'description', 'owner', 'appointment_time', 'appointment_date')


class ReceptionSerializer(serializers.ModelSerializer):
    # phone_number = serializers.CharField(max_length=30)
    # species = serializers.CharField(max_length=20)
    # year_of_birth = serializers.DateField()

    class Meta:
        model = Reception
        fields = (
            'id', 'appointment', 'doctor', 'owner_name', 'related_owner_name', 'pet', 'price', 'date', 'temperature',
            'preliminary_diagnosis', 'appointments', 'send_to_email', 'recommended_researches', 'weight', 'gender',
            'phone_number', 'species', 'year_of_birth', 'breed', 'address'
        )

    def create(self, validated_data):
        reception = super().create(validated_data)
        reception.save()
        receptions_id = reception.pk
        v_d = validated_data
        print(f'валидная инфа {v_d}')
        if v_d['related_owner_name'] is None:
            Pet.objects.create(name=v_d['pet'], year_of_birth=v_d['year_of_birth'], species=v_d['species'],
                               owner_name=v_d['owner_name'], gender=v_d['gender'], breed=v_d['breed'])
        create_docx(validated_data, receptions_id)
        return reception