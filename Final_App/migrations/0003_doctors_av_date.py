# Generated by Django 2.2.3 on 2019-07-31 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Final_App', '0002_auto_20190730_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='av_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
