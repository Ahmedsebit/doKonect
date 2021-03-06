from django import forms
from django.contrib.auth import get_user_model
from .models import Profile, DoctorProfile

User = get_user_model()


class UserRegistrationForm(forms.Form):

    REGISTRATION_CHOICES = (
        ('doctors', 'Doctor'),
        ('clinics', 'Clinic'),
    )

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    register_as = forms.CharField(max_length=10, widget=forms.Select(choices=REGISTRATION_CHOICES))

    def clean_password2(self):
        password= self.cleaned_data.get('password')
        password2= self.cleaned_data.get('password2')

        if password!=password2:
            raise forms.ValidationError("Password must match")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("Email is already registered")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phonenumber', 
            'location', 
            'name'
        ]

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
            'phonenumber', 
            'location', 
            'full_name',
            'doctor_type'
        ]

        