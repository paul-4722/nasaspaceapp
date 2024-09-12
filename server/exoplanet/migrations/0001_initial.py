# Generated by Django 5.1.1 on 2024-09-10 02:47

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
                ('username', models.CharField(error_messages={'unique': 'Already used!'}, max_length=100, primary_key=True, serialize=False, unique=True, validators=[exoplanet.models.validate_no_special_character])),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[exoplanet.models.validate_no_special_character])),
                ('size', models.FloatField()),
                ('owned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stars', to='exoplanet.author')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[exoplanet.models.validate_no_special_character])),
                ('size', models.FloatField()),
                ('owned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planets', to='exoplanet.author')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planets', to='exoplanet.star')),
            ],
        ),
    ]
