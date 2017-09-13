from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

from .models import Doctor_Referral

User = get_user_model()

class Doctor_ReferralTestCase(TestCase):
    def setUp(self):

        random_user = User.objects.create(username='testadmin')

    def test_refferal_creation(self):
        obj = Doctor_Referral.objects.create(
            user = User.objects.first(),
            patient_id = "patient_id",
            doctor_id = "doctor_id",
            booked_date = "booked_date",
            group = "group"
        )
        self.assertTrue(obj.patient_id ==  "patient_id")
        self.assertTrue(obj.id ==  1)
