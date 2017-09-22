from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100)

    def __str__(self):
        return (self.firstname)

    def get_absolute_url(self):
        return reverse("patients:detail", kwargs={"pk":self.pk})

    class Meta:
        ordering = ['-firstname']

class PatientVisit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField(max_length=1000, default='Anonymous')
    service_requested = models.TextField(max_length=200, default='Anonymous')
    user_id = models.TextField(settings.AUTH_USER_MODEL)
    service_type_requested = models.TextField(max_length=200, default='Anonymous')
    referral_reason = models.TextField(max_length=2000, default='Anonymous')

    def __str__(self):
        return self.diagnosis

    def get_absolute_url(self):
        return reverse('patient', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date']

