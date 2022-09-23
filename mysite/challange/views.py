from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from challange.models import Name, Week, Score

# Create your views here.
class ChallangeView(View):
    def get(self, request):
        text = "help me figure this out please"
        wn = Name.objects.all().count()
        context = {'text': text, 'wholename': wn}
        return render(request, 'challange/challangemain.html', context)

class NameCreate(CreateView):
    model = Name
    fields = '__all__'
    success_url = reverse_lazy('challange:NameCreate')