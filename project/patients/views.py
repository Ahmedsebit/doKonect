from django import forms
from django.forms.utils import ErrorList
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
# from .mixins import FormUserNeededMixins, UserOwnerMixins

from .forms import Patient_Form, PatientVisit_Form
from .models import Patient, PatientVisit

# Create your views here.
class Patient_CreateView(LoginRequiredMixin, CreateView):
    form_class = Patient_Form
    template_name = 'patients/patients_create.html'

    def form_valid(self, form):
        # form.instance.patient_id = self.kwargs['patient_id']
        form.instance.user = self.request.user
        return super(Patient_CreateView, self).form_valid(form)


class Patient_UpdateView(LoginRequiredMixin, UpdateView):
    queryset = Patient.objects.all()
    form_class = Patient_Form
    template_name = 'patients/patients_update.html'

class Patient_DeleteView(DeleteView):
    model = Patient
    template_name = 'patients/patients_delete.html'
    success_url = reverse_lazy("patients:list") 

class Patient_DetailView(LoginRequiredMixin, DetailView):
    
    queryset = Patient.objects.all()
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Patient.objects.get(id=pk)

class Patient_ListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Patient.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) 
                )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(Patient_ListView, self).get_context_data(*args, **kwargs)
        return context

'''
PatientVisit Details
'''
class PatientVisit_CreateView(LoginRequiredMixin, CreateView):
    form_class = PatientVisit_Form
    template_name = 'patients/patientsvisit_create.html'
    success_url = '/patients/'

    def form_valid(self, form):
        form.instance.patient_id = self.kwargs['patient_id']
        form.instance.user_id = self.request.user
        return super(PatientVisit_CreateView, self).form_valid(form)


class PatientVisit_UpdateView(LoginRequiredMixin, UpdateView):
    queryset = PatientVisit.objects.all()
    form_class = PatientVisit_Form
    template_name = 'patients/patientsvisit_update.html'


class PatientVisit_DeleteView(LoginRequiredMixin, DeleteView):
    model = PatientVisit
    template_name = 'patients/patientsvisit_delete.html'
    success_url = reverse_lazy("patients:list") 


class PatientVisit_DetailView(LoginRequiredMixin, DetailView):
    queryset = PatientVisit.objects.all()
    def get_object(self):
        pk = self.kwargs.get('pk')
        return PatientVisit.objects.get(id=pk)


class PatientVisitAll_ListView(LoginRequiredMixin, ListView):
    def get_queryset(self, *args, **kwargs):
        qs = PatientVisit.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) 
                )
        return qs


class PatientVisitPatient_ListView(LoginRequiredMixin, ListView):
    template_name = 'patients/patientvisit_list.html'
    def get_queryset(self, *args, **kwargs):
        patient_id = self.kwargs.get('patient_id')
        qs = PatientVisit.objects.all()

        if patient_id is not None:
            qs = qs.filter(
                Q(patient=patient_id) 
                )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(PatientVisitPatient_ListView, self).get_context_data(*args, **kwargs)
        return context

class PatientVisitPatient_DetailView(LoginRequiredMixin, DetailView):
    queryset = PatientVisit.objects.all()
    def get_object(self):
        pk = self.kwargs.get('pk')
        patient_id = self.kwargs.get('patient_id')
        return PatientVisit.objects.get(id=pk, patient=patient_id)