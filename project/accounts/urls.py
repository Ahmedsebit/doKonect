from django.conf.urls import url
from .views import (
    UserDetailView
)

urlpatterns = [
    # url(r'^create/$', Doctor_Referral_CreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/update/$', Doctor_Referral_UpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', Doctor_Referral_DeleteView.as_view(), name='delete'),
    # url(r'^$', Doctor_Referral_ListView.as_view(), name='list'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
]

