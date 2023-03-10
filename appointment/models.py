from django.db import models

from users.models import DoctorProfile, PetOwnerProfile, Pet

class Reception(models.Model):

     """ model for adding doctor appointment """

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, verbose_name='Doctor')
    owner = models.ForeignKey(PetOwnerProfile, on_delete=models.CASCADE, verbose_name='Owner')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Pet')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Price')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Reception date')
    temperature = models.DecimalField(max_digits=2,decimal_places=1, verbose_name='Temperature')
    preliminary_diagnosis = models.CharField(max_length=254, verbose_name='Preliminary diagnosis')
    appointments = models.TextField(verbose_name='Doctor\'s appointments')
    send_to_email = models.BooleanField(verbose_name='Do you want to send PDF version to email?')

