from django.contrib import admin

# Register your models here.
from .models import Doctor_Referral

from .forms import Doctor_Referral_Form


class Doctor_Referral_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = Doctor_Referral
        

admin.site.register(Doctor_Referral, Doctor_Referral_Admin)