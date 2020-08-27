# Generated by Django 3.1 on 2020-08-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_answer_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='insta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='results',
            field=models.ImageField(default='results.png', upload_to='results'),
        ),
        migrations.AddField(
            model_name='location',
            name='results_mobile',
            field=models.ImageField(default='results-mobile.png', upload_to='results'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time answered'),
        ),
    ]
