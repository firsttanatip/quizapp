# Generated by Django 2.2.7 on 2020-02-20 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_questions_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='image',
        ),
    ]
