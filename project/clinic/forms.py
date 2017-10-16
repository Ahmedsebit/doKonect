from django import forms

from .models import Clinic_Date


class Clinic_Date_Form(forms.ModelForm):

    class Meta:
        model = Clinic_Date
        fields = [
            "clinic_name",
            "clinic_details",
            "clinic_date",
        ]

