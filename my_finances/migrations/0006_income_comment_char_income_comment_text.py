# Generated by Django 4.0.4 on 2022-05-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_finances', '0005_alter_income_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='comment_char',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='comment_text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
