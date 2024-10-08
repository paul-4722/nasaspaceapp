# Generated by Django 5.1.1 on 2024-10-06 02:22

import django.db.models.deletion
import exoplanet.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(error_messages={'unique': 'Already used!'}, max_length=100, primary_key=True, serialize=False, unique=True, validators=[exoplanet.models.validate_string])),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('points', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoplanet.author')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('planets_number', models.IntegerField()),
                ('spectral_type', models.CharField(blank=True, max_length=100, null=True)),
                ('effective_temp', models.FloatField(blank=True, null=True)),
                ('radius', models.FloatField(blank=True, null=True)),
                ('mass', models.FloatField(blank=True, null=True)),
                ('luminosity', models.FloatField(blank=True, null=True)),
                ('azi', models.FloatField(default=0)),
                ('pol', models.FloatField(default=0)),
                ('visual_magnitude', models.FloatField(blank=True, null=True)),
                ('habitable_min', models.FloatField(blank=True, null=True)),
                ('habitable_max', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('owned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stars', to='exoplanet.author')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semimajor_axis', models.FloatField(blank=True, null=True)),
                ('radius', models.FloatField(blank=True, null=True)),
                ('mass', models.FloatField(blank=True, null=True)),
                ('density', models.FloatField(blank=True, null=True)),
                ('eccentricity', models.FloatField(blank=True, default=0, null=True)),
                ('insolation', models.FloatField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('escape_vel', models.FloatField(blank=True, null=True)),
                ('ESI', models.FloatField(blank=True, null=True)),
                ('SType', models.CharField(max_length=10)),
                ('TType', models.CharField(max_length=10)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('magnetic_field', models.CharField(blank=True, max_length=100, null=True)),
                ('albedo', models.FloatField(blank=True, null=True)),
                ('rotation_period', models.FloatField(blank=True, null=True)),
                ('atmospheric_pressure', models.FloatField(blank=True, null=True)),
                ('atmospheric_composition', models.CharField(blank=True, max_length=100, null=True)),
                ('tilt', models.FloatField(default=0, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_by_user', models.BooleanField(default=False)),
                ('owned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planets', to='exoplanet.author')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planets', to='exoplanet.star')),
            ],
        ),
    ]
