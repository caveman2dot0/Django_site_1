from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class CoolView(View):
    def coolit(request):
        context = {
            "level" : "easy",
            "word" : "apple"
        }
        return render(request, "coolit/coolitview.html", context)