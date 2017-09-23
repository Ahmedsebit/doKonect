from django.contrib import admin

# Register your models here.
from .models import Profile

from .forms import ProfileForm


class Profile_Admin(admin.ModelAdmin):
    # form  = Doctor_Referral_Form
    class meta:
        model = Profile
        

admin.site.register(Profile, Profile_Admin)