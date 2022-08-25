from django.shortcuts import render
from django.views import View
from os.path import exists

import os
import os.path
import random
# Create your views here.

class PasswordView(View):
    def get(self, request):
        return render(request, 'passwordgen/maingen.html')

class EasyView(View):
    def get(self, request):
        return render(request, 'passwordgen/easygen.html')

class MediumView(View):
    def get(self, request):
    	length = 2
    	passwordmedium = ""
    	path_file = os.path.join(os.path.dirname(__file__), 'shortword2.txt')
    	x = sum(1 for line in open(path_file)) #counts how many lines/words are in the file to make random range
    	file = open(path_file)
    	content = file.readlines()
    	while length > 0:
    		spot = random.randint(1, x)
    		word = content[spot-1]
    		passwordmedium += word.rstrip("\n")
    		length -= 1
    	number = "1234567890"
    	go = 2
    	while go > 0:
    	    spot = random.randint(1,10)
    	    passwordmedium += number[spot-1]
    	    go -= 1
    	special = "!$#"
    	lap = 1
    	while lap > 0:
    	    spot = random.randint(1,3)
    	    passwordmedium += special[spot-1]
    	    lap -= 1
    	file.close()
    	context = {'passwordmedium' : ": "+passwordmedium}
    	return render(request, 'passwordgen/mediumgen.html', context)
