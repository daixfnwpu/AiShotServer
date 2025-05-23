# Generated by Django 5.1.1 on 2024-10-16 23:01

import django.db.models.deletion
from django.db import migrations, models


def add_rubber_width_choices(apps, schema_editor):
    RubberWidth = apps.get_model('AiShotServer', 'RubberWidth')
    RubberWidth.objects.create(width='18')
    RubberWidth.objects.create(width='20')
    RubberWidth.objects.create(width='25')
    RubberWidth.objects.create(width='30')

def add_rubber_thickness_choices(apps, schema_editor):
    RubberThickness = apps.get_model('AiShotServer', 'RubberThickness')
    RubberThickness.objects.create(thickness='0.45')
    RubberThickness.objects.create(thickness='0.50')
    RubberThickness.objects.create(thickness='0.55')
    RubberThickness.objects.create(thickness='0.60')
    RubberThickness.objects.create(thickness='0.65')
    RubberThickness.objects.create(thickness='0.70')
    RubberThickness.objects.create(thickness='0.75')
    RubberThickness.objects.create(thickness='0.80')
    RubberThickness.objects.create(thickness='0.85')
    RubberThickness.objects.create(thickness='0.90')
    RubberThickness.objects.create(thickness='0.95')
    RubberThickness.objects.create(thickness='1')
    
def add_initial_rubber_length_choices(apps, schema_editor):
    InitialRubberLength = apps.get_model('AiShotServer', 'InitialRubberLength')
    InitialRubberLength.objects.create(length='0.18')
    InitialRubberLength.objects.create(length='0.19')
    InitialRubberLength.objects.create(length='0.20')
    InitialRubberLength.objects.create(length='0.21')
    InitialRubberLength.objects.create(length='0.22')
    InitialRubberLength.objects.create(length='0.23')
    InitialRubberLength.objects.create(length='0.24')
    InitialRubberLength.objects.create(length='0.25')
        
class Migration(migrations.Migration):
    dependencies = [
        ("AiShotServer", "0031_alter_initialrubberlength_length"),
    ]

    operations = [
        
        migrations.RemoveField(
            model_name="initialrubberlength",
            name="device_profile",
        ),
        migrations.RemoveField(
            model_name="rubberthickness",
            name="device_profile",
        ),
        migrations.RemoveField(
            model_name="rubberwidth",
            name="device_profile",
        ),
        
        migrations.RunPython(add_rubber_width_choices),
        migrations.RunPython(add_rubber_thickness_choices),
        migrations.RunPython(add_initial_rubber_length_choices),
        
        
        
        migrations.AlterField(
            model_name="deviceprofile",
            name="initlengthofrubber_m",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="AiShotServer.initialrubberlength",
            ),
        ),
        migrations.AlterField(
            model_name="deviceprofile",
            name="thinofrubber_mm",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="AiShotServer.rubberthickness",
            ),
        ),
        migrations.AlterField(
            model_name="deviceprofile",
            name="widthofrubber_mm",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="AiShotServer.rubberwidth",
            ),
        ),
    ]
