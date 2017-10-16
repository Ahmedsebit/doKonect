from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from .pagination import StandardResultsPagination
from doctor_referral.models import Doctor_Referral
from .serializers import Doctor_ReferralSerializer

class Doctor_ReferralCreateAPIView(generics.CreateAPIView):
    serializer_class = Doctor_ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class Doctor_ReferralListAPIView(generics.ListAPIView):
    serializer_class = Doctor_ReferralSerializer
    pagination_class = StandardResultsPagination
    
    def get_queryset(self, *args, **kwargs):
        
        qs = Doctor_Referral.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(patient_id__icontains=query) |
                Q(doctor_id__icontains=query) 
                )
        return qs