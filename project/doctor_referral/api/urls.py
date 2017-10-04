from django.conf.urls import url
from .views import (
    Doctor_ReferralListAPIView,
    Doctor_ReferralCreateAPIView
)

urlpatterns = [
    url(r'^$', Doctor_ReferralListAPIView.as_view(), name='list'),
    
    url(r'^create/$', Doctor_ReferralCreateAPIView.as_view(), name='create'),
]

