from django.conf.urls import url, include
from .views import (
    UserDetailView,
    UserProfileDetailView,
    UserProfileCreateView,
    DoctorProfileCreateView,
    DoctorProfileDetailView,
)

urlpatterns = [
    # url(r'^(?P<pk>\d+)/update/$', Doctor_Referral_UpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', Doctor_Referral_DeleteView.as_view(), name='delete'),
    # url(r'^$', Doctor_Referral_ListView.as_view(), name='list'),
    url(r'^create/$', UserProfileCreateView.as_view(), name='create'),
    url(r'^create_doctor/$', DoctorProfileCreateView.as_view(), name='create_profile'),
    # url(r'^(?P<username>[\w.@+-]+)/$', UserProfileDetailView.as_view(), name='detail'),
    url(r'^$', UserProfileDetailView.as_view(), name='profile'),
    url(r'^doctor/$', DoctorProfileDetailView.as_view(), name='doctor'),
]

