# Generated by Django 3.0.7 on 2020-06-26 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20200626_0425'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email',
            new_name='StaffEmail',
        ),
    ]