from django import forms

from .models import Patient, PatientVisit

class Patient_Form(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
            "firstname",
            "lastname",
            "dob",
            "gender",
            "phonenumber",
            "address",
            "email"
        ]

        
class PatientVisit_Form(forms.ModelForm):
    
    class Meta:
        model = PatientVisit
        fields = [
            "diagnosis",
            "service_requested",
            "service_type_requested",
            "referral_reason"
        ]

    