from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from .views import UserDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^main/', main, name='main'),
    url(r'^referral/', include('doctor_referral.urls', namespace='referral')),
    url(r'^api/referral/', include('doctor_referral.api.urls', namespace='referral-api')),
]

if settings.DEBUG:
    urlpatterns+= (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))