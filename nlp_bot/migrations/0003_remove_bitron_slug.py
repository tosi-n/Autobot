# Generated by Django 2.2 on 2020-04-12 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nlp_bot', '0002_auto_20200412_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitron',
            name='slug',
        ),
    ]
