# Generated by Django 3.2.4 on 2021-11-08 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0020_alter_patient_d_o_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.CharField(default=datetime.date(2021, 11, 7), max_length=20),
        ),
    ]
