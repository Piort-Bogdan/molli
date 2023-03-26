# Generated by Django 4.1.7 on 2023-03-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_rename_recommended_research_reception_recommended_researches_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reception',
            name='gender',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('FINISHED', 'FINISHED'), ('CANCELED', 'CANCELED'), ('CONFIRMED', 'CONFIRMED'), ('NEW', 'NEW')], default='NEW', max_length=9),
        ),
    ]