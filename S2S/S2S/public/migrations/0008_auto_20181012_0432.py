# Generated by Django 2.1 on 2018-10-12 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0007_auto_20181012_0416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='method',
            new_name='rent_type',
        ),
    ]
