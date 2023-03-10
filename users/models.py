from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ User custom model """

    job_title = models.CharField(max_length=100, verbose_name='Job title')
    name = models.CharField(max_length=200, verbose_name='Full name')
    phone_number = models.CharField(max_length=30, verbose_name='Phone number')
    address = models.CharField(max_length=254, verbose_name='Address')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Pet(models.Model):

    """ Model adding pet """

    name = models.CharField(max_length=100, verbose_name='Pet\'s name')
    year_of_birth = models.DateField('Year of birth')
    species = models.CharField(max_length=100, verbose_name='Species')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Pet owner', related_name='Pets')

    def __str__(self):
        return self.name



