# Generated by Django 2.1 on 2018-09-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_merge_20180827_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
