# Generated by Django 4.1.7 on 2023-03-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('CANCELED', 'CANCELED'), ('NEW', 'NEW'), ('CONFIRMED', 'CONFIRMED')], max_length=9),
        ),
    ]
