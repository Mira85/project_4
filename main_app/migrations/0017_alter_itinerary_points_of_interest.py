# Generated by Django 4.0.3 on 2022-03-22 17:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_itinerary_points_of_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='points_of_interest',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=220), blank=True, default=list, size=None),
        ),
    ]
