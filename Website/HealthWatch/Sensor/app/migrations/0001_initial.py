# Generated by Django 4.2.4 on 2023-08-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoredData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerical_value', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
