# Generated by Django 3.1.2 on 2020-10-04 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nv_profile', '0002_nvroom_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='nvuserprofile',
            name='last_active_room',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
