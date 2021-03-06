# Generated by Django 2.1 on 2018-10-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_lease_period_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id', models.IntegerField()),
                ('title', models.CharField(max_length=256)),
                ('area', models.CharField(max_length=128)),
                ('method', models.CharField(choices=[('S', 'Share'), ('W', 'Whole')], default='S', max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('mobile', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.AlterField(
            model_name='house_comment',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='house_picture',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='house_rate',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='house_tag',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='lease_period',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_rate',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_tag',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
