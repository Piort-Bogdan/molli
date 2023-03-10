from django.db import models
from django.core.validators import MinValueValidator


class Medicament(models.Model):

    """ model adding medicament in veterinary pharmacy """

    name = models.CharField(max_length=100, verbose_name='Medicament\'s name')
    description = models.TextField(verbose_name='Description')
    img = models.ImageField(upload_to='media/medicine_img/%Y/%m/%d/', verbose_name='Image')
    count = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Count')
    medicament_form = models.CharField(max_length=100, verbose_name='Medicament form')
    article = models.CharField(max_length=50, verbose_name='Article')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Price')
    barcode = models.CharField(max_length=50, verbose_name='Barcode')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Medicament'
        verbose_name_plural = 'Medicament'
        ordering = ('name', )


class Manufacturer(models.Model):

    """ adding manufacturer of medicament """

    name = models.CharField(max_length=100, verbose_name='Name')
    country = models.CharField(max_length=100, verbose_name='Country')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
        ordering = ('country', )


class Pharmacy(models.Model):

    """ model relating medicament and manufacturer in veterinary pharmacy """

    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='medicaments')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturers')

    def __str__(self):
        return f'{self.medicament}, {self.manufacturer}'
