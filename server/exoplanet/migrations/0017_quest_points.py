# Generated by Django 5.1.1 on 2024-10-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoplanet', '0016_remove_planet_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='points',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
