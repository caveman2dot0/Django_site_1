from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'challange'
urlpatterns = [
    path('', views.ChallangeView.as_view(), name='challange'),
    path('NameCreate/', views.NameCreate.as_view(), name='NameCreate')
]