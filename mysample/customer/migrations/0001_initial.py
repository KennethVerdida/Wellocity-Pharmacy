# Generated by Django 3.1.1 on 2020-10-11 09:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRegistered_Medicine', models.DateField(default=django.utils.timezone.now)),
                ('sku', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('genericName', models.CharField(max_length=100)),
                ('commonBrand', models.CharField(max_length=100)),
                ('manufacturedDate', models.DateField(default=django.utils.timezone.now)),
                ('expiryDate', models.DateField(default=django.utils.timezone.now)),
                ('size', models.FloatField()),
                ('order', models.IntegerField()),
                ('total', models.FloatField()),
                ('howTo_Use', models.CharField(max_length=100)),
                ('sideEffects', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('noItems', models.IntegerField()),
                ('img1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'Medicine',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('middleName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=50)),
                ('barangay', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('Zip', models.IntegerField()),
                ('province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('religion', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('spouseName', models.CharField(max_length=50)),
                ('spouseOccupation', models.CharField(max_length=50)),
                ('noChildren', models.IntegerField()),
                ('motherName', models.CharField(max_length=50)),
                ('motherOccupation', models.CharField(max_length=50)),
                ('fatherName', models.CharField(max_length=50)),
                ('fatherOccupation', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customer.person')),
                ('dateRegistered_Customer', models.DateField(default=django.utils.timezone.now)),
                ('profilePicture', models.FileField(default='settings.MEDIA_ROOT/default.png', upload_to='')),
                ('medicines', models.ManyToManyField(to='customer.Medicine')),
            ],
            options={
                'db_table': 'Customer',
            },
            bases=('customer.person',),
        ),
    ]
