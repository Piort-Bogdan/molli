# Generated by Django 4.1.7 on 2023-03-25 23:40

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='owner',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Owner's name"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='users.pet', verbose_name='Pet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reception',
            name='doctor',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_receptions', to=settings.AUTH_USER_MODEL, verbose_name='Doctor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reception',
            name='gender',
            field=models.CharField(choices=[('female', 'F'), ('male', 'M')], default=12, max_length=6, verbose_name='Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reception',
            name='owner',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='owner_receptions', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reception',
            name='pet',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='users.pet', verbose_name='Pet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reception',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=12, max_digits=4, verbose_name="Pet's weight"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 3, 25))], verbose_name='Appointment date'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('FINISHED', 'FINISHED'), ('CONFIRMED', 'CONFIRMED'), ('CANCELED', 'CANCELED')], default='NEW', max_length=9),
        ),
        migrations.AlterField(
            model_name='reception',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Temperature'),
        ),
    ]
