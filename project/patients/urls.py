from django.conf.urls import url
from .views import (
    Patient_CreateView,
    Patient_DeleteView,
    Patient_DetailView,
    Patient_ListView,
    Patient_UpdateView,
    PatientVisit_CreateView,
    PatientVisit_DeleteView,
    PatientVisit_DetailView,
    PatientVisitPatient_ListView,
    PatientVisitPatient_DetailView,
    PatientVisit_UpdateView
    
)

urlpatterns = [
    url(r'^add/$', Patient_CreateView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/update/$', Patient_UpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', Patient_DeleteView.as_view(), name='delete'),
    url(r'^$', Patient_ListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', Patient_DetailView.as_view(), name='detail'),
    #patient visit
    url(r'^(?P<patient_id>\d+)/referral/add/$', PatientVisit_CreateView.as_view(), name='addreferral'),
    url(r'^(?P<patient_id>\d+)/referral/(?P<pk>\d+)/update/$', PatientVisit_UpdateView.as_view(), name='updatereferral'),
    url(r'^(?P<patient_id>\d+)/referral/(?P<pk>\d+)/delete/$', PatientVisit_DeleteView.as_view(), name='deletereferral'),
    url(r'^(?P<patient_id>\d+)/referral/$', PatientVisitPatient_ListView.as_view(), name='listreferral'),
    url(r'^(?P<patient_id>\d+)/referral/(?P<pk>\d+)/$', PatientVisitPatient_DetailView.as_view(), name='detailreferral'),
]

