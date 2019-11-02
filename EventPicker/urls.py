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
from django.template.context_processors import static
from django.urls import path
from  EventApp import views
from EventPicker import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', views.log, name='log'),
    path('', views.index, name='index'),
    path('forget/', views.forget, name='forget'),
    path('regis/', views.regis, name='registration'),
    path('event/', views.event, name='event'),
    path('addevent/', views.addevent, name='addevent'),
    path('editevent/', views.editevent, name='editevent'),
    path('viewevent/', views.viewevent, name='viewevent'),
]
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)