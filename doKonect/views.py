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
        return HttpResponseRedirect(reverse_lazy("clinic:cliniclist"))
    elif request.user.groups.filter(name='doctors').exists():
        return HttpResponseRedirect(reverse_lazy("clinic:doctorlist"))
    else:
        return HttpResponseRedirect(reverse_lazy("clinic:list"))