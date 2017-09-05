from django.conf.urls import url
from .views import (
    Doctor_Referral_CreateView,
    Doctor_Referral_UpdateView,
    Doctor_Referral_DetailView, 
    Doctor_Referral_ListView,
    Doctor_Referral_DeleteView
)

urlpatterns = [
    url(r'^create/$', Doctor_Referral_CreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', Doctor_Referral_UpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', Doctor_Referral_DeleteView.as_view(), name='delete'),
    url(r'^$', Doctor_Referral_ListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', Doctor_Referral_DetailView.as_view(), name='detail'),
]

