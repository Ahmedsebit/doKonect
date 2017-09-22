from django.contrib import admin

# Register your models here.
from .models import Patient, PatientVisit

from .forms import Patient_Form


class Patient_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = Patient

class PatientVisit_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = PatientVisit
        

admin.site.register(Patient, Patient_Admin)
admin.site.register(PatientVisit, PatientVisit_Admin)
