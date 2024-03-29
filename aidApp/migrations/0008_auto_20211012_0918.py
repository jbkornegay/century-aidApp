# Generated by Django 3.2.4 on 2021-10-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0007_auto_20211007_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_address_1',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_address_2',
            new_name='address_2',
        ),
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_phone_number',
            new_name='relation',
        ),
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_state',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='emergency_contact_info',
            old_name='ec_zip_code',
            new_name='zip_code',
        ),
        migrations.AddField(
            model_name='emergency_contact_info',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='smoker',
            field=models.CharField(default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='app_status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Accept'), (2, 'Decline')], default=0),
        ),
    ]
