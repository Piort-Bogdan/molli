from django.db import models
from django.contrib.auth.models import User


class DoctorProfile(models.Model):

    """ Doctor profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Full name')
    job_title = models.CharField(max_length=100, verbose_name='Job title')
    phone_number = models.CharField(max_length=30, verbose_name='Phone number')
    email = models.EmailField(max_length=254, verbose_name='E-mail')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ('job_title', )


class PetOwnerProfile(models.Model):

    """ Pet owner profile model """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Full name')
    phone_number = models.CharField(max_length=30, verbose_name='Phone number')
    email = models.EmailField(max_length=254, verbose_name='E-mail')
    address = models.CharField(max_length=254, verbose_name='Address')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pet owner'
        verbose_name_plural = 'Pet owners'


class Pet(models.Model):

    """ Model adding pet """

    name = models.CharField(max_length=100, verbose_name='Pet\'s name')
    year_of_birth = models.DateField('Year of birth')
    species = models.CharField(max_length=100, verbose_name='Species')
    owner = models.ForeignKey(PetOwnerProfile, on_delete=models.CASCADE, verbose_name='Pet owner', related_name='Pets')

    def __str__(self):
        return self.name



