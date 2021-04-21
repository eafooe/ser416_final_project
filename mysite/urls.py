"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
   # path('admin/', admin.site.urls),
    
#]
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^services/$', views.services, name='programs'),
    url(r'^rentals/$', views.rentals, name='rentals'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^reservations/$', views.reservations, name='reservations'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.svg')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^employee-login/$', auth_views.LoginView.as_view(template_name="registration/employee-login.html"), name='employee-login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dummy/$', views.dummy, name='dummy'),
    url(r'^book', views.book, name='book'),
    url(r'^unbook', views.unbook, name='unbook'),
    url(r'^addCard', views.addCard, name='addCard'),
    url(r'^donation', views.donation, name='donation'),
    url(r'^add_offering', views.add_offering, name='add_offering'),
    url(r'^deleteOffering', views.deleteOffering, name='deleteOffering'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

