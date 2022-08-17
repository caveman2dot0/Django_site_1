import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView
from . import views


#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#SITE_ROOT = os.path.join(BASE_DIR, 'site')

app_name = 'giveitem'

urlpatterns = [
   # path('', views.home),
    path('', views.GoView.as_view(), name='gomain'),
    path('temp', views.TempView.as_view(), name='gotemp'),
    path('animal', views.AnimalView.as_view(), name='animal'),
    path('mobile', views.CarView.as_view(), name='mobile'),
    ]