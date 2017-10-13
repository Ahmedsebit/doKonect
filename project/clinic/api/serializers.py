from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from clinic.models import Clinic_Date, Clinic_Date_Patients
from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer 
from patients.api.serializers import PatientVisitSerializer


class Clinic_DateDisplaySerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()
    class Meta:
        model = Clinic_Date
        user_id = UserDisplaySerializer(read_only=True)
        fields = [
            'id',
            'clinic_name',
            'clinic_details',
            'user_id',
            'booking_date',
            'clinic_date',
            'doctor_accept',
            'clinic_accept',
            'clinic_type'
        ]

    def get_referal_count(self, obj):
        return 0

    def get_url(self, obj):
        return reverse_lazy("clinic:list", kwargs={"username":obj.username})


class Clinic_Date_PatientDisplaySerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()
    class Meta:
        model = Clinic_Date_Patients
        user = UserDisplaySerializer(read_only=True)
        clinic = Clinic_DateDisplaySerializer(read_only=True)
        patient = PatientVisitSerializer(read_only=True)
        fields = [
            'clinic',
            'user',
            'patient',
            'date'
        ]

    def get_referal_count(self, obj):
        return 0

    def get_url(self, obj):
        return reverse_lazy("clinic:list", kwargs={"username":obj.username})