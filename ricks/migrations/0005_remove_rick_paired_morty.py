# Generated by Django 5.0.4 on 2024-05-10 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricks', '0004_rick_paired_morty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rick',
            name='paired_morty',
        ),
    ]
