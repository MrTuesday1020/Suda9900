from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('landord_id', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('postcode', models.IntegerField()),
                ('price', models.IntegerField()),
                ('profile', models.TextField(null=True)),
                ('max_guests', models.IntegerField()),
                ('no_of_beds', models.IntegerField()),
                ('no_of_bedrooms', models.IntegerField()),
                ('no_of_baths', models.IntegerField()),
                ('no_of_parking', models.IntegerField()),
                ('tv', models.BooleanField(default=False)),
                ('kitchen', models.BooleanField(default=False)),
                ('washer', models.BooleanField(default=False)),
                ('fridge', models.BooleanField(default=False)),
                ('conditioner', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('study_room', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('house_rule', models.TextField()),
                ('cancellation', models.TextField()),
                ('extra', models.TextField(null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'house',
            },
        ),
        migrations.CreateModel(
            name='House_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('tenant_id', models.IntegerField()),
                ('house_id', models.IntegerField()),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'house_comment',
            },
        ),
        migrations.CreateModel(
            name='House_Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('house_id', models.IntegerField()),
                ('photo', models.ImageField(upload_to=None)),
            ],
            options={
                'db_table': 'house_picture',
            },
        ),
        migrations.CreateModel(
            name='House_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('tenant_id', models.IntegerField()),
                ('accuracy', models.IntegerField()),
                ('communication', models.IntegerField()),
                ('cleanliness', models.IntegerField()),
                ('location', models.IntegerField()),
                ('check_in', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'db_table': 'house_rate',
            },
        ),
        migrations.CreateModel(
            name='House_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('house_id', models.IntegerField()),
                ('tag_id', models.IntegerField()),
            ],
            options={
                'db_table': 'house_tag',
            },
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to=None)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('dob', models.DateField(null=True)),
                ('profile', models.TextField(null=True)),
                ('activate', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'landlord',
            },
        ),
        migrations.CreateModel(
            name='Lease_Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('house_id', models.IntegerField()),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
            ],
            options={
                'db_table': 'lease_period',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to=None)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('dob', models.DateField(null=True)),
                ('profile', models.TextField(null=True)),
                ('activate', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tenant',
            },
        ),
        migrations.CreateModel(
            name='Tenant_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('tenant_id', models.IntegerField()),
                ('landlord_id', models.IntegerField()),
                ('reputation', models.IntegerField()),
            ],
            options={
                'db_table': 'tenant_rate',
            },
        ),
        migrations.CreateModel(
            name='Tenant_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('tenant_id', models.IntegerField()),
                ('tag_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tenant_tag',
            },
        ),
    ]
