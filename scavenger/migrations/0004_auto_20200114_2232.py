# Generated by Django 3.0.1 on 2020-01-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger', '0003_scavengerhunt_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scavengerhunt',
            name='players_phone_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
