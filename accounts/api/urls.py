from django.conf.urls import url
from .views import (
    PatientCreateAPIView,
    PatientListAPIView,
    PatientVisitCreateAPIView,
    PatientVisitListAPIView,
    PatientVisitPatientListAPIView
)

urlpatterns = [
    url(r'^$', PatientListAPIView.as_view(), name='list'),
    url(r'^create/$', PatientCreateAPIView.as_view(), name='add'),
    url(r'^referral/$', PatientVisitListAPIView.as_view(), name='listreferrals'),
    url(r'^(?P<patient_id>\d+)/referral/$', PatientVisitPatientListAPIView.as_view(), name='listpatientreferral'),
    url(r'^referral/create/(?P<patient_id>\d+)/$', PatientVisitCreateAPIView.as_view(), name='addreferral'),
]

