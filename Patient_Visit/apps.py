from django.apps import AppConfig


class PatientVisitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Patient_Visit'

    def ready(self):
        import Patient_Visit.signals