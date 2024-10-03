# Generated by Django 5.1.1 on 2024-10-03 14:58

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
                ('name', models.CharField(error_messages={'unique': 'Already used!'}, max_length=100, primary_key=True, serialize=False, unique=True, validators=[exoplanet.models.validate_no_special_character])),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[exoplanet.models.validate_no_special_character])),
                ('description', models.CharField(max_length=1000)),
                ('completed', models.BooleanField()),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoplanet.author')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[exoplanet.models.validate_no_special_character])),
                ('planets_number', models.IntegerField()),
                ('spectral_type', models.CharField(max_length=100)),
                ('effective_temp', models.IntegerField()),
                ('mass', models.FloatField()),
                ('radius', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('owned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stars', to='exoplanet.author')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[exoplanet.models.validate_no_special_character])),
                ('semimajor_axis', models.FloatField()),
                ('eccentricity', models.FloatField()),
                ('mass', models.FloatField()),
                ('radius', models.FloatField()),
                ('magnetic_field', models.CharField(blank=True, max_length=100, null=True)),
                ('albedo', models.FloatField(blank=True, null=True)),
                ('rotation_period', models.FloatField(blank=True, null=True)),
                ('atmospheric_pressure', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('owned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planets', to='exoplanet.author')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planets', to='exoplanet.star')),
            ],
        ),
    ]
