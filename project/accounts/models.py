from django.db import models
from patients.models import DoctorServices

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=500, blank=True)
    name = models.TextField(max_length=500, blank=True)

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=500, blank=True)
    full_name = models.TextField(max_length=500, blank=True)
    doctor_type = models.ForeignKey(DoctorServices, on_delete=models.CASCADE)