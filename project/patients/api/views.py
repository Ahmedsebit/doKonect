from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from .pagination import StandardResultsPagination
from patients.models import Patient, PatientVisit
from .serializers import PatientSerializer, PatientVisitSerializer

class PatientCreateAPIView(generics.CreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class PatientListAPIView(generics.ListAPIView):
    serializer_class = PatientSerializer
    pagination_class = StandardResultsPagination
    
    def get_queryset(self, *args, **kwargs):
        
        qs = Patient.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) 
                )
        return qs

class PatientVisitCreateAPIView(generics.CreateAPIView):
    serializer_class = PatientVisitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class PatientVisitListAPIView(generics.ListAPIView):
    serializer_class = PatientVisitSerializer
    pagination_class = StandardResultsPagination
    
    def get_queryset(self, *args, **kwargs):
        qs = PatientVisit.objects.all()
        return qs


class PatientVisitPatientListAPIView(generics.ListAPIView):
    serializer_class = PatientVisitSerializer
    pagination_class = StandardResultsPagination
    
    def get_queryset(self, *args, **kwargs):
        patient_id = self.kwargs.get('patient_id')
        qs = PatientVisit.objects.all()

        if patient_id is not None:
            qs = qs.filter(
                Q(patient=patient_id) 
                )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(PatientVisitPatientListAPIView, self).get_context_data(*args, **kwargs)
        return context