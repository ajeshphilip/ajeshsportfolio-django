# Generated by Django 4.0.4 on 2022-05-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0004_pollutantentry_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollutant',
            name='limit_value',
            field=models.SmallIntegerField(null=True),
        ),
    ]
