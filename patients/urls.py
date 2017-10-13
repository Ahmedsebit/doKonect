from django.conf.urls import url
from .views import (
    Patient_CreateView,
    Patient_DeleteView,
    Patient_DetailView,
    ClinicPatient_DetailView,
    Patient_ListView,
    ClinicPatient_ListView,
    Patient_UpdateView,
    PatientVisit_CreateView,
    ClinicPatientVisit_CreateView,
    PatientVisit_DeleteView,
    PatientVisit_DetailView,
    ClinicPatientVisit_DetailView,
    PatientVisitPatient_ListView,
    PatientVisitPatient_DetailView,
    ClinicPatientVisitPatient_DetailView,
    PatientVisit_UpdateView
    
)

urlpatterns = [
    url(r'^add/$', Patient_CreateView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/update/$', Patient_UpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', Patient_DeleteView.as_view(), name='delete'),
    url(r'^$', Patient_ListView.as_view(), name='list'),
    url(r'^clinic/$', ClinicPatient_ListView.as_view(), name='cliniclist'),
    url(r'^(?P<pk>\d+)/$', Patient_DetailView.as_view(), name='detail'),
    url(r'^clinic/patient/(?P<pk>\d+)/$', ClinicPatient_DetailView.as_view(), name='clinicpatientdetail'),
    #patient visit
    url(r'^(?P<patient_id>\d+)/referral/add/$', PatientVisit_CreateView.as_view(), name='addreferral'),
    url(r'^clinic/patient/(?P<patient_id>\d+)/add/$', ClinicPatientVisit_CreateView.as_view(), name='clinicaddreferral'),
    url(r'^(?P<patient_id>\d+)/referral/(?P<pk>\d+)/update/$', PatientVisit_UpdateView.as_view(), name='updatereferral'),
    url(r'^(?P<patient_id>\d+)/referral/(?P<pk>\d+)/delete/$', PatientVisit_DeleteView.as_view(), name='deletereferral'),
    url(r'^(?P<patient_id>\d+)/referral/$', PatientVisitPatient_ListView.as_view(), name='listreferral'),
    url(r'^(?P<patient_id>\d+)/referral/(?P<pk>\d+)/$', PatientVisitPatient_DetailView.as_view(), name='detailreferral'),
    url(r'^(?P<patient_id>\d+)/clinic/(?P<pk>\d+)/$', ClinicPatientVisitPatient_DetailView.as_view(), name='detailclinicreferral'),
]

