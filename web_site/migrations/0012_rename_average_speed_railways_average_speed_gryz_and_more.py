# Generated by Django 5.0.2 on 2024-05-27 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0011_railways_current_move'),
    ]

    operations = [
        migrations.RenameField(
            model_name='railways',
            old_name='average_speed',
            new_name='average_speed_gryz',
        ),
        migrations.AddField(
            model_name='railways',
            name='average_speed_pass',
            field=models.FloatField(default=1),
        ),
    ]
