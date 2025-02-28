# Generated by Django 4.1.2 on 2022-10-08 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Patient_Files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patiant_Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mode_Name', models.CharField(blank=True, max_length=21, null=True)),
            ],
            options={
                'db_table': 'Patiant_Mode',
            },
        ),
        migrations.CreateModel(
            name='Pateint_Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reception', models.CharField(choices=[('OPD', 'OPD'), ('ER', 'ER')], default='ER', max_length=190)),
                ('Visit_Date', models.DateTimeField(auto_now_add=True)),
                ('ins_user_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_admission', models.BooleanField(default=False)),
                ('admission_from_visit_case_id', models.CharField(blank=True, max_length=100, null=True)),
                ('is_Close', models.BooleanField(default=False)),
                ('Closed_Date', models.DateField(blank=True, null=True)),
                ('Close_Details', models.CharField(blank=True, max_length=100, null=True)),
                ('Clinic_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Clinic_Name_%(class)s_objects', to='App_Home.clinic_list')),
                ('Close_By_User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Close_By_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('Patiant_Mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mod', to='Patient_Visit.patiant_mode')),
                ('Patiant_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Patiant', to='Patient_Files.patiant_file_no')),
                ('ins_user_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Patient_Visit',
            },
        ),
    ]
