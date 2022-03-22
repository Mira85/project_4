# Generated by Django 4.0.3 on 2022-03-22 17:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_itinerary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='points_of_interest',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=220), null=True, size=None),
        ),
    ]
