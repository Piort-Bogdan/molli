# Generated by Django 4.1.7 on 2023-03-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'CONFIRMED'), ('CANCELED', 'CANCELED'), ('NEW', 'NEW')], max_length=9),
        ),
    ]