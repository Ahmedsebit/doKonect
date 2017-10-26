from django.contrib import admin

# Register your models here.
from .models import Profile, DoctorProfile

from .forms import ProfileForm, DoctorProfileForm


class Profile_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = Profile
        
class DoctorProfile_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = DoctorProfile
        
admin.site.register(DoctorProfile, DoctorProfile_Admin)
admin.site.register(Profile, Profile_Admin)