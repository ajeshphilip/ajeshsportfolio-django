# Generated by Django 4.0.4 on 2022-05-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_finances', '0007_remove_income_comment_char_balance_user_income_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='date',
            field=models.DateField(default='2021-10-10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
