from django.db import models

from users.models import DoctorProfile, PetOwnerProfile, Pet


class Reception(models.Model):

    """ model for adding doctor appointment """

    doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE, verbose_name='Doctor')
    owner = models.ForeignKey('PetOwnerProfile', on_delete=models.CASCADE, verbose_name='Owner')
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, verbose_name='Pet')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Price')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Reception date')
    temperature = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Temperature')
    preliminary_diagnosis = models.CharField(max_length=254, verbose_name='Preliminary diagnosis')
    appointments = models.TextField(verbose_name='Doctor\'s appointments')
    send_to_email = models.BooleanField(verbose_name='Do you want to send PDF version to email?')

    def __str__(self):
        return f'Doctor - {self.doctor},Pet name - {self.pet},'

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'


class Appointment(models.Model):

    """ model for adding application for a doctor's appointment """

    STATUS = {
        ('NEW', 'NEW'),
        ('CANCELED', 'CANCELED'),
        ('CONFIRMED', 'CONFIRMED'),
    }

    pet = models.ForeignKey(Pet, verbose_name='Pet', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Problem description')
    owner = models.ForeignKey('PetOwnerProfile', verbose_name='Owner\' name', on_delete=models.CASCADE)
    status = models.CharField(max_length=9, choices=STATUS)
    appointment_time = models.TimeField('%h-%m-%s')
    appointment_date = models.DateField('%Y-%d-%m')