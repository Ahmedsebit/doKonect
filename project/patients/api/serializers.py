from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer 
from patients.models import Patient, PatientVisit

class PatientSerializer(serializers.ModelSerializer):

    # user_id = UserDisplaySerializer(read_only=True)
    class Meta:
        model = Patient
        fields = [
            "id",
            "firstname",
            "lastname",
            "dob",
            "gender",
            "phonenumber",
            "address",
            "email"
        ]

class PatientVisitSerializer(serializers.ModelSerializer):

    patient = PatientSerializer(read_only=True)
    class Meta:
        model = PatientVisit
        fields = [
            "patient",
            "diagnosis",
            "service_requested",
            "service_type_requested",
            "referral_reason",
            "user_id"
        ]