from django import forms
from django.forms.utils import ErrorList
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .mixins import FormUserNeededMixins, UserOwnerMixins

from .forms import Doctor_Referral_Form
from .models import Doctor_Referral

# Create your views here.
class Doctor_Referral_CreateView(LoginRequiredMixin, FormUserNeededMixins, CreateView):
    form_class = Doctor_Referral_Form
    template_name = 'doctor_referral/doctor_referral_create.html'


class Doctor_Referral_UpdateView(LoginRequiredMixin, UserOwnerMixins, UpdateView):
    queryset = Doctor_Referral.objects.all()
    form_class = Doctor_Referral_Form
    template_name = 'doctor_referral/doctor_referral_update.html'
    login_url = '/admin/'


class Doctor_Referral_DeleteView(LoginRequiredMixin, FormUserNeededMixins, DeleteView):
    model = Doctor_Referral
    template_name = 'doctor_referral/confirm_delete.html'
    success_url = reverse_lazy("referral:list") 


class Doctor_Referral_DetailView(LoginRequiredMixin, DetailView):
    queryset = Doctor_Referral.objects.all()
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Doctor_Referral.objects.get(id=pk)


class Doctor_Referral_ListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):        
        qs = Doctor_Referral.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(patient_id__icontains=query) |
                Q(doctor_id__icontains=query) 
                )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(Doctor_Referral_ListView, self).get_context_data(*args, **kwargs)
        return context
