# Generated by Django 5.1.1 on 2024-09-10 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exoplanet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='username',
            new_name='name',
        ),
    ]
