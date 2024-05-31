# Generated by Django 5.0.2 on 2024-05-23 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0003_room_railways_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='railways',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='railways',
            name='name',
            field=models.CharField(default='Unnamed Railway', max_length=100),
        ),
        migrations.AlterField(
            model_name='railways',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_site.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
