# Generated by Django 2.2.7 on 2020-02-19 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20200219_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
