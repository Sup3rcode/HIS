# Generated by Django 4.1.2 on 2022-10-08 16:43

import Patient_Files.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(blank=True, max_length=3, null=True)),
                ('country_desc', models.CharField(blank=True, max_length=25, null=True)),
                ('area_code', models.CharField(blank=True, max_length=2, null=True)),
                ('male_nationality_desc', models.CharField(blank=True, max_length=16, null=True)),
                ('female_nationality_desc', models.CharField(blank=True, max_length=16, null=True)),
                ('country_e_desc', models.CharField(blank=True, max_length=23, null=True)),
                ('nationality_e_desc', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'Nationality',
            },
        ),
        migrations.CreateModel(
            name='Patiant_File_NO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('patiant_no', models.IntegerField()),
                ('ar_patiant_name', models.CharField(blank=True, max_length=200, null=True)),
                ('en_patiant_name', models.CharField(blank=True, max_length=200, null=True)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=200, null=True)),
                ('social_number', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_no', models.IntegerField(blank=True)),
                ('mother_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_med_no', models.IntegerField(blank=True, null=True)),
                ('patiant_no_form', models.CharField(blank=True, max_length=200, null=True)),
                ('smok_status', models.CharField(blank=True, max_length=200, null=True)),
                ('ins_user_date', models.DateField(auto_now_add=True, null=True)),
                ('upd_user_date', models.DateField(blank=True, null=True)),
                ('mother_id', models.IntegerField(blank=True, null=True)),
                ('ID_image', models.ImageField(blank=True, null=True, upload_to=Patient_Files.models.Patient_Files_ID_Images)),
                ('ins_user_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Patiant_File_NO_insert_user_code', to=settings.AUTH_USER_MODEL)),
                ('nationalty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Patient_Files.nationality')),
                ('upd_user_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Patiant_File_NO',
            },
        ),
        migrations.CreateModel(
            name='Archives_Patient_Files_Scanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Patient_Files.models.Archives_Patient_Files)),
                ('Scan_Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('By_User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Patiant_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Archive_Patient_Files', to='Patient_Files.patiant_file_no')),
            ],
        ),
    ]
