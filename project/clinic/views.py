from django.contrib.auth import get_user_model
from django import forms
from django.forms.utils import ErrorList
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .mixins import FormUserNeededMixins, UserOwnerMixins

from .forms import Clinic_Date_Form
from .models import Clinic_Date, Clinic_Date_Patients
from accounts.models import DoctorProfile
from patients.models import PatientVisit, Patient

User = get_user_model()

# Create your views here.
class Clinic_Date_CreateView(LoginRequiredMixin, FormUserNeededMixins, CreateView):
    form_class = Clinic_Date_Form
    template_name = 'clinic/clinic_date_create.html'

    def form_valid(self, form):
        # form.instance.patient_id = self.kwargs['patient_id']
        this_user = DoctorProfile.objects.get(user=self.request.user)
        form.instance.user = self.request.user
        form.instance.clinic_type = this_user.doctor_type
        form.instance.doctor_accept = 'True'
        return super(Clinic_Date_CreateView, self).form_valid(form)


class Clinic_Date_UpdateView(LoginRequiredMixin, UserOwnerMixins, UpdateView):
    queryset = Clinic_Date.objects.all()
    form_class = Clinic_Date_Form
    template_name = 'clinic/clinic_date_update.html'

class Clinic_Date_MainUpdateView(LoginRequiredMixin, UpdateView):
    form_class = Clinic_Date_Form
    template_name = 'clinic/clinic_date_update.html'


class Clinic_Date_DeleteView(LoginRequiredMixin, FormUserNeededMixins, DeleteView):
    model = Clinic_Date
    template_name = 'clini/confirm_delete.html'
    success_url = reverse_lazy("clinic:list") 


class Clinic_Date_DetailView(LoginRequiredMixin, DetailView):
    queryset = Clinic_Date.objects.all()
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Clinic_Date.objects.get(id=pk)


class Clinic_Date_MainClinicDetailView(LoginRequiredMixin, DetailView):
    queryset = Clinic_Date.objects.all()
    template_name = 'clinic/mainclinic_detail_view.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        clinic = Clinic_Date.objects.get(id=pk)
        try:
            clinic_patients = Clinic_Date_Patients.objects.filter(
                                                            Q(clinic__id__iexact=clinic.id)
                                                            )
            context = {'clinic':clinic, 'clinic_patients':clinic_patients}
            return context
        except:
            clinic_patients = Clinic_Date_Patients.objects.filter(
                                                            Q(clinic__id__iexact=clinic.id)
                                                            )
            context = {'clinic':clinic, 'clinic_patients':None}
            return context



class Clinic_Date_ClinicDetailView(LoginRequiredMixin, DetailView):
    queryset = Clinic_Date.objects.all()
    template_name = 'clinic/allclinic_detail_view.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        clinic = Clinic_Date.objects.get(id=pk)
        patients = PatientVisit.objects.all()
        try:
            clinic_patients = Clinic_Date_Patients.objects.filter(
                                                            Q(clinic__id__iexact=clinic.id)
                                                            )
            clinic_object = {'clinic':clinic, 'clinic_patients':clinic_patients, 'patients':patients}
            return clinic_object
        except:
            patients = PatientVisit.objects.all()
            clinic_object = {'clinic':clinic, 'clinic_patients':None, 'patients':patients}
            return clinic_object

class Clinic_Date_DoctorDetailView(LoginRequiredMixin, DetailView):
    queryset = Clinic_Date.objects.all()
    template_name = 'clinic/doctorclinic_detail_view.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        clinic = Clinic_Date.objects.get(id=pk)
        patients = PatientVisit.objects.all()
        try:
            clinic_patients = Clinic_Date_Patients.objects.filter(
                                                            Q(clinic__id__iexact=clinic.id)
                                                            )
            clinic_object = {'clinic':clinic, 'clinic_patients':clinic_patients, 'patients':patients}
            return clinic_object
        except:
            patients = PatientVisit.objects.all()
            clinic_object = {'clinic':clinic, 'clinic_patients':None, 'patients':patients}
            return clinic_object




class Clinic_Date_ListView(LoginRequiredMixin, ListView):

    template_name = 'clinic/clinic_date_list.html'
    def get_queryset(self, *args, **kwargs):        
        qs = Clinic_Date.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(clinic_name__icontains=query)
                )
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super(Clinic_Date_ListView, self).get_context_data(*args, **kwargs)
        return context


class Clinic_Date_DoctorListView(LoginRequiredMixin, ListView):

    template_name = 'clinic/clinic_date_doctorlist.html'
    def get_queryset(self, *args, **kwargs):        
        qs = Clinic_Date.objects.all()
        qs = qs.filter(
                Q(user_id__username__iexact=self.request.user)
                )
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(clinic_name__icontains=query)
                )
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super(Clinic_Date_DoctorListView, self).get_context_data(*args, **kwargs)
        return context

class Clinic_Date_ClinicListView(LoginRequiredMixin, ListView):

    template_name = 'clinic/clinic_date_cliniclist.html'
    def get_queryset(self, *args, **kwargs):        
        qs = Clinic_Date.objects.all()
        qs = qs.filter(
                Q(clinic_accept__iexact='Accepted')
                )
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(clinic_name__icontains=query)
                )
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super(Clinic_Date_ClinicListView, self).get_context_data(*args, **kwargs)
        return context


def accept_view(request, *args, **kwargs):
    my_obj = Clinic_Date.objects.filter(pk=kwargs['id'])
    if my_obj:
        my_obj = my_obj[0]
        my_obj.clinic_accept = "Accepted"
        my_obj.save()
    return HttpResponseRedirect(reverse_lazy("clinic:list"))

def reject_view(request, *args, **kwargs):
    my_obj = Clinic_Date.objects.filter(pk=kwargs['id'])
    if my_obj:
        my_obj = my_obj[0]
        my_obj.clinic_accept = "Rejected"
        my_obj.save()
    return HttpResponseRedirect(reverse_lazy("clinic:list"))

def addpatient_view(request, *args, **kwargs):
    my_obj = Clinic_Date.objects.get(pk=kwargs['clinic_id'])
    patient_obj = Patient.objects.get(pk=kwargs['patient_id'])
    user = User.objects.get(username=request.user)
    print (user)
    new_patient = Clinic_Date_Patients.objects.create(clinic=my_obj, user=user, patient=patient_obj)
    new_patient.save()
    return HttpResponseRedirect(reverse_lazy("clinic:cliniclist"))