from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=500, blank=True)
    name = models.TextField(max_length=500, blank=True)