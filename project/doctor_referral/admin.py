from django.contrib import admin

# Register your models here.
from .models import Doctor_Referral

from .forms import Doctor_Referral_Form


class Doctor_Referral_Admin(admin.ModelAdmin):
    class meta:
        model = Doctor_Referral
        form  = Doctor_Referral_Form

admin.site.register(Doctor_Referral, Doctor_Referral_Admin)