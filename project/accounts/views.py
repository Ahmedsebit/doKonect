from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .forms import UserRegistrationForm
from .forms import ProfileForm, DoctorProfileForm
from .models import Profile, DoctorProfile
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

User = get_user_model()

class UserRegistrationView(FormView):
    template_name = 'accounts/user_register_form.html'
    form_class = UserRegistrationForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        register_as = form.cleaned_data.get("register_as")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email, password=password)
        new_user.set_password(password)
        group = Group.objects.get(name=register_as)
        new_user.groups.add(group)
        new_user.save()
        return super(UserRegistrationView, self).form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()
    
    def get_object(self):
        username = self.kwargs.get('username')
        return User.objects.get(username=username)


class UserProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = ProfileForm
    template_name = 'accounts/user_profile_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserProfileCreateView, self).form_valid(form)


class DoctorProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = DoctorProfileForm
    template_name = 'accounts/doctor_profile_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DoctorProfileCreateView, self).form_valid(form)


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user_profile.html'
    def get_object(self):
        username = self.kwargs.get('username')
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return None


class DoctorProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/doctor_profile.html'
    def get_object(self):
        username = self.kwargs.get('username')
        try:
            return DoctorProfile.objects.get(user=self.request.user)
        except DoctorProfile.DoesNotExist:
            return None