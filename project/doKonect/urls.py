"""doKonect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home, main
from accounts.views import UserRegistrationView
from doKonect import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^main/', main, name='main'),
    url(r'^referral/', include('doctor_referral.urls', namespace='referral')),
    url(r'^clinic/', include('clinic.urls', namespace='clinic')),
    url(r'^patients/', include('patients.urls', namespace='patients')),
    url(r'^api/referral/', include('doctor_referral.api.urls', namespace='referral-api')),
    url(r'^api/patients/', include('patients.api.urls', namespace='patients-api')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^register/', UserRegistrationView.as_view(), name='register'),
    url(r'^profiles/', include('accounts.urls', namespace='profiles')),
    url(r'login_success/$', views.login_success, name='login_success')
]

if settings.DEBUG:
    urlpatterns+= (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))