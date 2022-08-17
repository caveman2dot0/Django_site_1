from django.shortcuts import render
from giveitem.models import GoList

from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import re
import os
import os.path
from os.path import exists
import random
#from giveitem import carlist


class GoView(View):
    def get(self, request):
        return render(request, 'giveitem/maintemp.html')

class TempView(View):
    def get(self, request):
        templist = ["hot", "cold", "burning", "freezing"]
        tempplace = random.randint(1,4)
        temp = (templist[tempplace-1])
        tempcontext = {
        "temp" : ": "+temp,
        "place" : (tempplace-1)
        }
        return render(request, 'giveitem/maintemp.html', tempcontext)

class AnimalView(View):
    def get(self, request):
        list1 = ["goat", "monkey", "hippo", "dog", "bee"]
        place = random.randint(1,5)
        animal = (list1[place-1])
        animalcontext = {
            "animal" : ": "+animal,
            "spot" : (place-1)
        }
        print(animal)
        return render(request, 'giveitem/maintemp.html', animalcontext)

class CarView(View):
    def get(self, request):
        path_file = os.path.join(os.path.dirname(__file__), 'carlist.txt')
        with open(path_file) as file:
            cart = file.readlines()
            spot = random.randint(1,8)
            cart = cart[spot-1]
            #cart = "banana"
            mobile = { 'cart' : ": "+cart }
        return render(request, 'giveitem/maintemp.html', mobile)
