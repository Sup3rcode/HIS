# Generated by Django 4.1.2 on 2022-10-08 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Patient_Files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section_Name', models.CharField(max_length=21, unique=True)),
                ('User_Access', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Admission_Section',
            },
        ),
        migrations.CreateModel(
            name='Admission_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_Number', models.CharField(max_length=21)),
                ('STATUS', models.CharField(choices=[('In Use', 'In Use'), ('Close', 'Close')], default='In Use', max_length=100)),
                ('ROOM_SEX', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='In Use', max_length=100)),
                ('MIXED_SEX', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=100)),
                ('Vacant', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=100)),
                ('DESCRIPTION', models.CharField(choices=[('Semi Private', 'Semi Private'), ('Isolation', 'Isolation'), ('Nursery', 'Nursery')], default='Semi Private', max_length=100)),
                ('Section_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ward.admission_section')),
            ],
            options={
                'db_table': 'Admission_Room',
                'unique_together': {('Section_Name', 'Room_Number')},
            },
        ),
        migrations.CreateModel(
            name='Admission_Room_Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bed_Num', models.CharField(max_length=1)),
                ('is_activate', models.BooleanField(default=False)),
                ('in_Use', models.BooleanField(default=False)),
                ('Patient_No', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pateiant_No_Admission_Bed', to='Patient_Files.patiant_file_no')),
                ('Room_Num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ward.admission_room')),
            ],
            options={
                'db_table': 'Admission_Room_Bed',
                'unique_together': {('Room_Num', 'Bed_Num')},
            },
        ),
    ]
