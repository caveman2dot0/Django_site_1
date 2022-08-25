import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView
from . import views

app_name = 'passwordgen'

urlpatterns = [
    path('', views.PasswordView.as_view(), name='maingen'),
    path('easygen', views.EasyView.as_view(), name='easygen'),
    path('mediumgen', views.MediumView.as_view(), name='mediumgen'),
    ]