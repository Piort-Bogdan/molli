from datetime import date

from django.core.validators import MinValueValidator
from django.db import models

from users.models import User, Pet


class Reception(models.Model):

    """ model for adding doctor appointment """

    doctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Doctor', related_name='doctor_receptions')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', related_name='owner_receptions')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Pet')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Price')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Reception date')
    temperature = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Temperature')
    preliminary_diagnosis = models.CharField(max_length=254, verbose_name='Preliminary diagnosis')
    appointments = models.TextField(verbose_name='Doctor\'s appointments')
    send_to_email = models.BooleanField(verbose_name='Do you want to send PDF version to email?')
    recommended_research = models.CharField(max_length=254, verbose_name='Recommended research', blank=True)

    def __str__(self):
        return f'Doctor - {self.doctor.name},Pet name - {self.pet.name},'

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'


class Appointment(models.Model):

    """ model for adding application for a doctor's appointment """

    STATUS = {
        ('NEW', 'NEW'),
        ('CANCELED', 'CANCELED'),
        ('CONFIRMED', 'CONFIRMED'),
        ('FINISHED', 'FINISHED'),
    }

    pet = models.ForeignKey(Pet, verbose_name='Pet', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Problem description')
    owner = models.ForeignKey(User, verbose_name='Owner\'s name', on_delete=models.CASCADE)
    status = models.CharField(max_length=9, choices=STATUS, default='NEW')
    appointment_time = models.TimeField('Appointment time')
    appointment_date = models.DateField(verbose_name='Appointment date',
                                        validators=[MinValueValidator(limit_value=date.today())], )
