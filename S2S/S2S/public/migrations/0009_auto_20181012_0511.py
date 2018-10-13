# Generated by Django 2.1 on 2018-10-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_auto_20181012_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_rooms',
            field=models.CharField(choices=[('A', 'All'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_type',
            field=models.CharField(choices=[('A', 'All'), ('S', 'Share'), ('W', 'Whole')], default='A', max_length=1),
        ),
    ]
