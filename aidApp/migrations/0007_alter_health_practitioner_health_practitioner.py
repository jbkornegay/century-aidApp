# Generated by Django 3.2.4 on 2021-10-05 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aidApp', '0006_auto_20211001_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_practitioner',
            name='health_practitioner',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
