from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from .pagination import StandardResultsPagination
from django.shortcuts import render, get_object_or_404
# from .mixins import FormUserNeededMixins, UserOwnerMixins

from .serializers import Clinic_Date_PatientDisplaySerializer, Clinic_DateDisplaySerializer
from django.core.mail import send_mail

from accounts.models import DoctorProfile
from clinic.models import Clinic_Date, Clinic_Date_Patients
from patients.models import Patient, PatientVisit
User = get_user_model()

# Create your views here.
class Clinic_Date_ApiCreateView(generics.CreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def form_valid(self, form):
        # form.instance.patient_id = self.kwargs['patient_id']
        this_user = DoctorProfile.objects.get(user=self.request.user)
        form.instance.user = self.request.user
        form.instance.clinic_type = this_user.doctor_type
        form.instance.doctor_accept = 'True'

        recepient = User.objects.get(username='shofco')

        send_mail(
        'New CLinic', 'A new clinic has been created.', 
        this_user.email, 
        [recepient], 
        fail_silently=False
        )
        
        return super(Clinic_Date_ApiCreateView, self).form_valid(form)


class Clinic_Date_DoctorApiCreateView(generics.CreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def form_valid(self, form):
        # form.instance.patient_id = self.kwargs['patient_id']
        this_user = DoctorProfile.objects.get(user=self.request.user)
        form.instance.user = self.request.user
        form.instance.clinic_type = this_user.doctor_type
        form.instance.doctor_accept = 'True'

        recepient = User.objects.get(username='shofco')

        send_mail(
        'New CLinic', 'A new clinic has been created.', 
        this_user.email, 
        [recepient], 
        fail_silently=False
        )

        return super(Clinic_Date_DoctorApiCreateView, self).form_valid(form)


class Clinic_Date_ApiUpdateView(generics.ListCreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

class Clinic_Date_MainApiUpdateView(generics.ListCreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]


class Clinic_Date_ApiDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated] 


class Clinic_Date_ApiDetailView(generics.ListCreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Clinic_Date.objects.get(id=pk)


class Clinic_Date_MainClinicApiDetailView(generics.ListCreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
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



class Clinic_Date_ClinicApiDetailView(generics.ListCreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
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


class Clinic_Date_DoctorApiDetailView(generics.ListCreateAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
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


class Clinic_Date_ApiListView(generics.ListAPIView):
    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
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


class Clinic_Date_DoctorApiListView(generics.ListAPIView):

    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
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


class Clinic_Date_ClinicApiListView(generics.ListAPIView):

    serializer_class = Clinic_DateDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
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


# def accept_view(request, *args, **kwargs):
#     my_obj = Clinic_Date.objects.filter(pk=kwargs['id'])
#     sender = User.objects.get(username='shofco')
#     if my_obj:
#         my_obj = my_obj[0]
#         my_obj.clinic_accept = "Accepted"
#         my_obj.save()

#     send_mail(
#         'Clinic Status', 'Clinic has been approved.', 
#         sender, 
#         [my_obj.user_id.email], 
#         fail_silently=False
#         )

#     return HttpResponseRedirect(reverse_lazy("clinic:list"))

# def reject_view(request, *args, **kwargs):
#     my_obj = Clinic_Date.objects.filter(pk=kwargs['id'])
#     sender = User.objects.get(username='shofco')
#     if my_obj:
#         my_obj = my_obj[0]
#         my_obj.clinic_accept = "Rejected"
#         my_obj.save()

#     send_mail(
#         'Clinic Status', 'Clinic has been rejeced.', 
#         sender,
#         [my_obj.user_id.email],
#         fail_silently=False
#         )

#     return HttpResponseRedirect(reverse_lazy("clinic:list"))


# def addpatient_view(request, *args, **kwargs):
#     my_obj = Clinic_Date.objects.get(pk=kwargs['clinic_id'])
#     patient_obj = Patient.objects.get(pk=kwargs['patient_id'])
#     sender = User.objects.get(username='shofco')
#     user = User.objects.get(username=request.user)
#     print (user)
#     new_patient = Clinic_Date_Patients.objects.create(clinic=my_obj, user=user, patient=patient_obj)
#     new_patient.save()
#     send_mail(
#         'New patient', 'A new patient has been added to the clinic.', 
#         user.email, 
#         [sender, my_obj.user_id.email], 
#         fail_silently=False
#         )

#     return HttpResponseRedirect(reverse_lazy("clinic:cliniclist"))
