from django.conf.urls import url
from .views import (
    Clinic_Date_DoctorCreateView,
    Clinic_Date_CreateView,
    Clinic_Date_UpdateView,
    Clinic_Date_DetailView,
    Clinic_Date_ClinicDetailView,
    Clinic_Date_DoctorDetailView,
    Clinic_Date_MainClinicDetailView, 
    Clinic_Date_ListView,
    Clinic_Date_DoctorListView,
    Clinic_Date_ClinicListView,
    accept_view,
    reject_view,
    addpatient_view
)

urlpatterns = [
    url(r'^myclinic/create/$', Clinic_Date_CreateView.as_view(), name='doctorcreate'),
    url(r'^create/$', Clinic_Date_CreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', Clinic_Date_UpdateView.as_view(), name='update'),
    url(r'^$', Clinic_Date_ListView.as_view(), name='list'),
    url(r'^myclinic/$', Clinic_Date_DoctorListView.as_view(), name='doctorlist'),
    url(r'^clinics/$', Clinic_Date_ClinicListView.as_view(), name='cliniclist'),
    url(r'^(?P<pk>\d+)/$', Clinic_Date_DetailView.as_view(), name='detail'),
    url(r'viewclinic/(?P<pk>\d+)/$', Clinic_Date_ClinicDetailView.as_view(), name='clinicdetail'),
    url(r'myscheduledclinic/(?P<pk>\d+)/$', Clinic_Date_DoctorDetailView.as_view(), name='clinicddetail'),
    url(r'^scheduledclinic/(?P<pk>\d+)/$', Clinic_Date_MainClinicDetailView.as_view(), name='cdetail'),
    url(r'^my_objects/(?P<id>\d+)/$', accept_view, name='accepted'),
    url(r'^my_objects/(?P<id>\d+)/$', reject_view, name='rejected'),
    url(r'^viewclinic/add_patient/(?P<clinic_id>\d+)/(?P<patient_id>\d+)/$', addpatient_view, name='add_patient')
]

