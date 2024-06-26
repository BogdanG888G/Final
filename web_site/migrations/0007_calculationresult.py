# Generated by Django 5.0.2 on 2024-05-24 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0006_alter_railways_pogryzka'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virychka_ot_gryzov', models.FloatField()),
                ('sebestoimost', models.FloatField()),
                ('financi_po_prochim', models.FloatField()),
                ('debitorka', models.FloatField()),
                ('kreditorka', models.FloatField()),
                ('pogruzka_gryzov', models.FloatField()),
                ('raspisanie_pass_poesdov', models.FloatField()),
                ('dolya_gryzovix_otpravok', models.FloatField()),
                ('average_speed', models.FloatField()),
                ('average_proivoditelnost_loko', models.FloatField()),
                ('time_zadershka', models.FloatField()),
                ('besopasnost', models.FloatField()),
                ('railway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.railways')),
            ],
        ),
    ]
