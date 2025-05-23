# Generated by Django 5.1.1 on 2024-10-06 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AiShotServer", "0017_alter_shotconfig_configui_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="shotconfig",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
