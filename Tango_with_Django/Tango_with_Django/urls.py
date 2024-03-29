"""Tango_with_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from registration.backends.simple.views import RegistrationView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
# from django.conf.urls import url
# from rango import views

# Create a new class that redirects the user to the index page,
#if successful at logging
class MyRegistrationView(RegistrationView):

    def get_success_url(self, user):
        return '/rango/'

urlpatterns = [
    # path('', views.index, name='index'),
    # url(r'^$', views.index, name='index'),

    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
    
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
]


