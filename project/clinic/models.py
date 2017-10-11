from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from .validators import validate_booked_date

from django.contrib.auth.models import User
from patients.models import Patient

# Create your models here.
class Clinic_Date(models.Model):
    clinic_name = models.CharField(max_length=100)
    clinic_details = models.CharField(max_length=1000)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    booking_date = models.DateTimeField(auto_now_add=True)
    clinic_date = models.DateTimeField(validators=[validate_booked_date])
    doctor_accept = models.CharField(max_length=250)
    clinic_accept = models.CharField(max_length=1000)
    clinic_type = models.CharField(max_length=100)

    def __str__(self):
        return (self.clinic_name)

    def get_absolute_url(self):
        return reverse("clinic:detail", kwargs={"pk":self.pk})

    class Meta:
        ordering = ['-clinic_date'] 

class Clinic_Date_Patients(models.Model):
    clinic = models.ForeignKey(Clinic_Date)
    user = models.ForeignKey(User)
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (str(self.clinic))

    class Meta:
        ordering = ['-date'] 
