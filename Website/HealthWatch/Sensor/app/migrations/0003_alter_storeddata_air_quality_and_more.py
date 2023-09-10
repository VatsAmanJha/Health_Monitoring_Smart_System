# Generated by Django 4.2.4 on 2023-08-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_storeddata_air_quality_storeddata_body_temp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeddata',
            name='air_quality',
            field=models.FloatField(default=150),
        ),
        migrations.AlterField(
            model_name='storeddata',
            name='body_temp',
            field=models.FloatField(default=98.6),
        ),
        migrations.AlterField(
            model_name='storeddata',
            name='env_temp',
            field=models.FloatField(default=88.0),
        ),
        migrations.AlterField(
            model_name='storeddata',
            name='pulse_rate',
            field=models.FloatField(default=75),
        ),
        migrations.AlterField(
            model_name='storeddata',
            name='spo2_level',
            field=models.FloatField(default=98),
        ),
    ]