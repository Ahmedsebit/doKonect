from django import forms

from .models import Doctor_Referral

class Doctor_Referral_Form(forms.ModelForm):

    class Meta:
        model = Doctor_Referral
        fields = [
            "patient_id",
            "doctor_id",
            "booked_date",
            "group",
            "comments"
        ]