from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer 
from doctor_referral.models import Doctor_Referral

class Doctor_ReferralSerializer(serializers.ModelSerializer):

    user_id = UserDisplaySerializer(read_only=True)
    class Meta:
        model = Doctor_Referral
        fields = [
            "user_id",
            "patient_id",
            "doctor_id",
            "booked_date",
            "group",
            "comments"
        ]