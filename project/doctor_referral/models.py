from django.conf import settings
from django.db import models

# Create your models here.
class Doctor_Referral(models.Model):
    patient_id = models.CharField(max_length=50)
    doctor_id = models.CharField(max_length=50)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    booking_date = models.DateTimeField(auto_now_add=True)
    booked_date = models.DateTimeField()
    group = models.CharField(max_length=250)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return (self.patient_id)
