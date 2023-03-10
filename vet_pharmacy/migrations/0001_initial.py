# Generated by Django 4.1.7 on 2023-03-10 21:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
                'ordering': ('country',),
            },
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Medicament's name")),
                ('description', models.TextField(verbose_name='Description')),
                ('img', models.ImageField(upload_to='media/medicine_img/%Y/%m/%d/', verbose_name='Image')),
                ('count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Count')),
                ('medicament_form', models.CharField(max_length=100, verbose_name='Medicament form')),
                ('article', models.CharField(max_length=50, verbose_name='Article')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price')),
                ('barcode', models.CharField(max_length=50, verbose_name='Barcode')),
            ],
            options={
                'verbose_name': 'Medicament',
                'verbose_name_plural': 'Medicament',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturers', to='vet_pharmacy.manufacturer')),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicaments', to='vet_pharmacy.medicament')),
            ],
        ),
    ]