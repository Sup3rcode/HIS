# Generated by Django 4.1 on 2022-10-17 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Home', '0001_initial'),
        ('Visit_Clinic', '0002_alter_pateint_visit_clinic_case_visit_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pateint_visit_clinic_case',
            name='Clinic_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pateint_Visit_Clinic_Name', to='App_Home.clinic_list'),
        ),
    ]