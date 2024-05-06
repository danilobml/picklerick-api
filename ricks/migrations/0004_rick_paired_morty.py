# Generated by Django 5.0.4 on 2024-05-06 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morties', '0003_remove_morty_paired_rick'),
        ('ricks', '0003_remove_rick_is_morty_alive'),
    ]

    operations = [
        migrations.AddField(
            model_name='rick',
            name='paired_morty',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paired_rick', to='morties.morty'),
        ),
    ]