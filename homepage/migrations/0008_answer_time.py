# Generated by Django 3.1 on 2020-08-26 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_location_hero_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='time answered'),
            preserve_default=False,
        ),
    ]
