# Generated by Django 2.2.5 on 2019-09-04 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ageprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='ageprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='age_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]