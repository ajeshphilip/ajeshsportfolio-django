# Generated by Django 4.0.4 on 2022-05-19 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_finances', '0006_income_comment_char_income_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='comment_char',
        ),
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='balances', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outcome',
            name='comment_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='income',
            name='comment_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]