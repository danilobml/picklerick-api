# Generated by Django 5.0.4 on 2024-04-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universe', models.CharField(max_length=255)),
                ('is_morty_alive', models.BooleanField()),
            ],
        ),
    ]
