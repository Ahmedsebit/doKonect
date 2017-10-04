from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return render(request, "home.html", {})

def main(request):
    return render(request, "main.html", {})


def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name='clinics').exists():
        # user is a clinic
        return HttpResponseRedirect(reverse_lazy("patients:list"))
    elif request.user.groups.filter(name='doctors').exists():
        return HttpResponseRedirect(reverse_lazy("referral:list"))
    else:
        return HttpResponseRedirect(reverse_lazy("referral:list"))