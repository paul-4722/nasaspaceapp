# Generated by Django 5.1.1 on 2024-10-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoplanet', '0004_remove_quest_completed_quest_progress_quest_target_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
