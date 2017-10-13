from django.conf.urls import url
from .views import (
    Clinic_Date_DoctorApiCreateView,
    Clinic_Date_ApiCreateView,
    Clinic_Date_ApiUpdateView,
    Clinic_Date_ApiDetailView,
    Clinic_Date_ClinicApiDetailView,
    Clinic_Date_DoctorApiDetailView,
    Clinic_Date_MainClinicApiDetailView, 
    Clinic_Date_ApiListView,
    Clinic_Date_DoctorApiListView,
    Clinic_Date_ClinicApiListView,
    # accept_view,
    # reject_view,
    # addpatient_view
)

urlpatterns = [
    url(r'^myclinic/create/$', Clinic_Date_ApiCreateView.as_view(), name='doctorcreate'),
    url(r'^create/$', Clinic_Date_ApiCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', Clinic_Date_ApiUpdateView.as_view(), name='update'),
    url(r'^$', Clinic_Date_ApiListView.as_view(), name='list'),
    url(r'^myclinic/$', Clinic_Date_DoctorApiListView.as_view(), name='doctorlist'),
    url(r'^clinics/$', Clinic_Date_ClinicApiListView.as_view(), name='cliniclist'),
    url(r'^(?P<pk>\d+)/$', Clinic_Date_ApiDetailView.as_view(), name='detail'),
    url(r'viewclinic/(?P<pk>\d+)/$', Clinic_Date_ClinicApiDetailView.as_view(), name='clinicdetail'),
    url(r'myscheduledclinic/(?P<pk>\d+)/$', Clinic_Date_DoctorApiDetailView.as_view(), name='clinicddetail'),
    url(r'^scheduledclinic/(?P<pk>\d+)/$', Clinic_Date_MainClinicApiDetailView.as_view(), name='cdetail'),
    # url(r'^my_objects/(?P<id>\d+)/$', accept_view, name='accepted'),
    # url(r'^my_objects/(?P<id>\d+)/$', reject_view, name='rejected'),
    # url(r'^viewclinic/add_patient/(?P<clinic_id>\d+)/(?P<patient_id>\d+)/$', addpatient_view, name='add_patient')
]

