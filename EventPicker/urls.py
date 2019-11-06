"""EventPicker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.template.context_processors import static
from django.urls import path, include
from  EventApp import views
from EventPicker import settings
from django.conf.urls.static import static
from django.contrib.auth.views import *
from django.conf import settings

urlpatterns = [
    path('', include('social_django.urls', namespace='index')),
    path('logout/', views.logout_google, name='logout_google'),
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.log, name='log'),
    path('forget/', views.forget, name='forget'),
    path('regis/', views.regis, name='registration'),
    path('event/', views.event, name='event'),
    path('addevent/', views.addevent, name='addevent'),
    path('editevent/', views.editevent, name='editevent'),
    path('eevent/', views.eevent, name='eevent'),
    path('testttable/', views.testttable, name='testttable'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('candidate_view/', views.candidate_view, name='candidate_view'),
    path('eventpub/',views.eventpub, name='eventpub')
]
urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns+= static(settings.MEDIA_URL_BROCHURES, document_root= settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()