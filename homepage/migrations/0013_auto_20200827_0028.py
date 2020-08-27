# Generated by Django 3.1 on 2020-08-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20200826_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='hi_text',
            field=models.CharField(blank=True, default='What was the <span class="hi">Hi</span> of this week?', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='lo_text',
            field=models.CharField(blank=True, default='What was the <span class="lo">Lo</span> of this week?', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]
