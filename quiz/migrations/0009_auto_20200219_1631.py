# Generated by Django 2.2.7 on 2020-02-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20200218_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ('-catagory',)},
        ),
        migrations.AlterField(
            model_name='questions',
            name='catagory',
            field=models.CharField(choices=[('sports', 'Sports'), ('movies', 'Movies'), ('maths', 'Maths'), ('generalknowledge', 'GeneralKnowledge')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
    ]
