from datetime import date

from django.core.validators import MinValueValidator
from django.db import models

from users.models import User, Pet


class Reception(models.Model):
    """ model for adding doctor appointment """

    doctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Doctor\'s name',
                               related_name='doctor_receptions')
    owner_name = models.CharField(max_length=255, verbose_name='Owner\'s full name', blank=True)
    breed = models.CharField(max_length=30, verbose_name='Pet\'s breed')
    related_owner_name = models.ForeignKey('users.Pet', on_delete=models.CASCADE, verbose_name='Owner\'s full name',
                                           blank=True, null=True)
    pet = models.CharField(max_length=255, verbose_name='Pet\'s name')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Price', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Reception date')
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Temperature', blank=True)
    preliminary_diagnosis = models.CharField(max_length=254, verbose_name='Preliminary diagnosis')
    appointments = models.TextField(verbose_name='Doctor\'s appointments')
    send_to_email = models.BooleanField(verbose_name='Do you want to send PDF version to email?')
    recommended_researches = models.CharField(max_length=254, verbose_name='Recommended research', blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Pet\'s weight(kg)')
    gender = models.CharField(max_length=6, verbose_name='Gender')
    appointment = models.OneToOneField('appointment.Appointment', on_delete=models.DO_NOTHING, blank=True,
                                       verbose_name='Select appointment', null=True)
    phone_number = models.CharField(max_length=30, verbose_name='Phone number')
    year_of_birth = models.DateField('Year of birth', blank=True)
    species = models.CharField(max_length=100, verbose_name='Species', blank=True)
    address = models.CharField(max_length=254, verbose_name='Address', blank=True)

    def __str__(self):
        return f'Doctor - {self.doctor.name}_{date}'

    class Meta:
        verbose_name = 'Reception'
        verbose_name_plural = 'Receptions'


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

    def __str__(self):
        return f'Имя: {self.owner.name}, Время: {self.appointment_time}'