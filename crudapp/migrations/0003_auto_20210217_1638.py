# Generated by Django 3.2 on 2021-02-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='temperature_summer',
            field=models.FloatField(default=float),
        ),
        migrations.AddField(
            model_name='countries',
            name='temperature_winter',
            field=models.IntegerField(default=int),
        ),
    ]
