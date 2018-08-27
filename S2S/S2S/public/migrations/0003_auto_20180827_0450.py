# Generated by Django 2.1 on 2018-08-27 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20180827_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_picture',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='house'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='user/default.png', upload_to='user'),
        ),
    ]
