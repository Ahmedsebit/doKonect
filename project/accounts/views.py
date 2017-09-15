from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .forms import UserRegistrationForm

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
        return get_object_or_404(
            User, 
            username__iexact=self.kwargs.get("username")
            )