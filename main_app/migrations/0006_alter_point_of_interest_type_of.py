# Generated by Django 4.0.3 on 2022-03-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_point_of_interest_remove_art_culture_neighborhood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point_of_interest',
            name='type_of',
            field=models.CharField(default='', max_length=100),
        ),
    ]
