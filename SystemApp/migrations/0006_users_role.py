# Generated by Django 3.2.9 on 2021-11-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemApp', '0005_rename_tarrifid_tarrif_tarrif_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
