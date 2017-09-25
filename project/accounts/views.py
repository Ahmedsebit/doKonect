from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .forms import UserRegistrationForm
from .forms import ProfileForm
from .models import Profile
# Create your views here.

User = get_user_model()

class UserRegistrationView(FormView):
    template_name = 'accounts/user_register_form.html'
    form_class = UserRegistrationForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email, password=password)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegistrationView, self).form_valid(form)


class UserDetailView(DetailView):

    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()
    
    def get_object(self):
        username = self.kwargs.get('username')
        return User.objects.get(username=username)


class UserProfileCreateView(CreateView):
    form_class = ProfileForm
    template_name = 'accounts/user_profile_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserProfileCreateView, self).form_valid(form)


class UserProfileDetailView(DetailView):

    template_name = 'accounts/user_profile.html'
    # queryset = User.objects.all()
    form_class = ProfileForm
    
    def get_object(self):
        username = self.kwargs.get('username')
        # profile = Profile.objects.get(user=self.request.user)
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return None