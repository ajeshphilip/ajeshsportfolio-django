# Generated by Django 4.0.4 on 2022-05-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_finances', '0002_income_repetition_interval_income_repetition_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='date',
        ),
        migrations.AddField(
            model_name='balance',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='date',
            field=models.DateField(),
        ),
    ]
