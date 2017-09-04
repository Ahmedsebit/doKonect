from django import forms

from .models import Doctor_Referral

class Doctor_Referral_Form(forms.ModelForm):
    class meta:
        model = Doctor_Referral
        fields = [
            "patient_id",
            "doctor_id",
            "booking_date",
            "booked_date",
            "group",
            "comments"
        ]