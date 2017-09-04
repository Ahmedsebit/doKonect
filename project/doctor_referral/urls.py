from django.conf.urls import url
from .views import Doctor_Referral_DetailView, Doctor_Referral_ListView

urlpatterns = [
    url(r'^$', Doctor_Referral_ListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', Doctor_Referral_DetailView.as_view(), name='detail'),
]

