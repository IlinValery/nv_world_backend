# Generated by Django 3.1.2 on 2020-10-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nv_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nvroom',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
