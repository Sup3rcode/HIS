# Generated by Django 4.1.2 on 2022-10-08 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Visit_Clinic', '0001_initial'),
        ('Admission', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Patient_Files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labotory_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(blank=True, max_length=50, null=True)),
                ('test_tybe', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Labotory_Test',
            },
        ),
        migrations.CreateModel(
            name='Labotory_Tube_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tube_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Tube_num', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Labotory_Tube_List',
            },
        ),
        migrations.CreateModel(
            name='Tube_Barcode_Number_admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tube_Test_Tybe', models.CharField(blank=True, max_length=50, null=True)),
                ('Tube_Number', models.CharField(blank=True, max_length=50, null=True)),
                ('Tube_Visit_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tube_Visit_addmiss', to='Admission.patient_admission_case_visit_section')),
            ],
            options={
                'db_table': 'Tube_Barcode_Number_admission',
            },
        ),
        migrations.CreateModel(
            name='Tube_Barcode_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tube_Test_Tybe', models.CharField(blank=True, max_length=50, null=True)),
                ('Tube_Number', models.CharField(blank=True, max_length=50, null=True)),
                ('Tube_Visit_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tube_Visit_Number', to='Visit_Clinic.pateint_visit_clinic_case')),
            ],
            options={
                'db_table': 'Tube_Barcode_Number',
            },
        ),
        migrations.CreateModel(
            name='test_save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_Visit_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_Visit_Number', to='Visit_Clinic.pateint_visit_clinic_case')),
                ('test_patient_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_patient_no', to='Patient_Files.patiant_file_no')),
            ],
        ),
        migrations.CreateModel(
            name='Specimens_Arrival_Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tube_Test_Name2', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('barcode_img', models.ImageField(blank=True, upload_to='images/Barcode')),
                ('is_Done', models.BooleanField(default=False)),
                ('ins_user_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Barcode_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Barcode_Number', to='labotory.tube_barcode_number')),
                ('Specimens_Visit_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Specimens_Visit_Number', to='Visit_Clinic.pateint_visit_clinic_case')),
                ('Tube_Test_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tube_Test_Name', to='labotory.labotory_test')),
                ('ins_user_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patiant_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pateiant_tube_Visit', to='Patient_Files.patiant_file_no')),
            ],
            options={
                'db_table': 'Specimens_Arrival_Visit',
            },
        ),
        migrations.CreateModel(
            name='Specimens_Arrival_admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tube_Test_Name2', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('barcode_img', models.ImageField(blank=True, upload_to='images/Barcode')),
                ('is_Done', models.BooleanField(default=False)),
                ('ins_user_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Admission_Visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Section_%(class)s_objects', to='Admission.patient_admission_case_visit_section')),
                ('Barcode_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Barcode%(class)s_objects', to='labotory.tube_barcode_number_admission')),
                ('Tube_Test_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tube%(class)s_objects', to='labotory.labotory_test')),
                ('ins_user_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patiant_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Patient_%(class)s_objects', to='Patient_Files.patiant_file_no')),
            ],
            options={
                'db_table': 'Specimens_Arrival_admission',
            },
        ),
    ]
