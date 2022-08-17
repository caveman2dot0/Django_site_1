from . import views
from django.urls import include, path
app_name = 'coolit'

urlpatterns = [
    path('coolit', views.CoolView.as_view(), name ='coolit'),
    ]