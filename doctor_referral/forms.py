from django import forms

from .models import Doctor_Referral, Clinic_ReferralDate

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

class Clinic_ReferralDate_Form(forms.ModelForm):

    class Meta:
        model = Clinic_ReferralDate
        fields = [
            "clinic_name",
            "clinic_date",
        ]

