# Generated by Django 3.2.4 on 2021-10-22 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0015_auto_20211021_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.CharField(default=datetime.date(2021, 10, 22), max_length=20),
        ),
    ]
