# Generated by Django 5.1.1 on 2024-09-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoplanet', '0002_rename_username_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
