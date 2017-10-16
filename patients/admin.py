from django.contrib import admin

# Register your models here.
from .models import Patient, PatientVisit, DoctorServices

from .forms import Patient_Form


class Patient_Admin(admin.ModelAdmin):

    class meta:
        model = Patient

class PatientVisit_Admin(admin.ModelAdmin):

    class meta:
        model = PatientVisit
        
class DoctorServices_Admin(admin.ModelAdmin):

    class meta:
        model = DoctorServices

admin.site.register(DoctorServices, DoctorServices_Admin)
admin.site.register(Patient, Patient_Admin)
admin.site.register(PatientVisit, PatientVisit_Admin)
