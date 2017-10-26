from django.contrib import admin
from .models import Clinic_Date, Clinic_Date_Patients
from .forms import Clinic_Date_Form

# Register your models here.

class Clinic_Date_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = Clinic_Date
        
class Clinic_Date_Patients_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = Clinic_Date_Patients

admin.site.register(Clinic_Date_Patients, Clinic_Date_Patients_Admin)
admin.site.register(Clinic_Date, Clinic_Date_Admin)