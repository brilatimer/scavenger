# Generated by Django 3.0.1 on 2020-01-07 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scavenger', '0002_auto_20200103_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='scavengerhunt',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scavenger_hunt', to=settings.AUTH_USER_MODEL),
        ),
    ]
