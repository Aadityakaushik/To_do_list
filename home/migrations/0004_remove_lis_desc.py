# Generated by Django 4.2.4 on 2023-08-11 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_contact_contact_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lis',
            name='desc',
        ),
    ]