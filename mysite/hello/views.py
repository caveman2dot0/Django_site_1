from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Links

# Create your views here.
def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    resp = HttpResponse("Hello World. 788d4162 view count="+str(num_visits))
    resp.set_cookie('dj4e_cookie', '788d4162', max_age=1000)
    return resp


