from django.shortcuts import render
from django.views import View
from os.path import exists

import os
import os.path
import random
# Create your views here.

def wordornum():
    lon = random.randint(1,4) #feeds a value to allow the generator to choose between placing a word or a number next
    if lon == 1:
        answer = "number"
    else:
        answer = "word"
    return answer

def numadder():
    number = random.randint(0,9) # picks a random number to place. more reuse of code c:
    return str(number)

class PasswordView(View):
    def get(self, request):

        return render(request, 'passwordgen/maingen.html')

class EasyView(View):
    def get(self, request):
        passwordeasy = ''
        numgo = 2
        path_file = os.path.join(os.path.dirname(__file__), 'longword2.txt')
        x = sum(1 for line in open(path_file)) #counts how many lines/words are in the file to make random range
        file = open(path_file)
        content = file.readlines()
        spot = random.randint(1,x)
        word = content[spot-1]
        passwordeasy = word.rstrip("\n")
        while numgo > 0:
            number = numadder()
            passwordeasy += number
            numgo -= 1
        file.close()
        context = {'passwordeasy' : ": "+passwordeasy}
        return render(request, 'passwordgen/easygen.html', context)

class MediumView(View):
    def get(self, request):
    	length = 2
    	gonum = 2
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
    		answer = wordornum()
    		if answer == "number":
    		    number = numadder()
    		    passwordmedium += number
    		    gonum -= 1
    	while gonum > 0:
    	    number = numadder()
    	    passwordmedium += number
    	    gonum -= 1
    	special = "!$#"
    	lap = 1
    	while lap > 0:
    	    spot = random.randint(1,3)
    	    passwordmedium += special[spot-1]
    	    lap -= 1
    	file.close()
    	context = {'passwordmedium' : ": "+passwordmedium}
    	return render(request, 'passwordgen/mediumgen.html', context)

class HardView(View):
    def get(self, request):
        length = 3 #how many times it grabs words
        passwordhard = ""
        gonum = 3
        path_shortfile = os.path.join(os.path.dirname(__file__), 'shortword2.txt')
        path_longfile = os.path.join(os.path.dirname(__file__), 'longword2.txt')
        lf = open(path_longfile)
        long = lf.readlines()
        sf = open(path_shortfile)
        short = sf.readlines()
        shortlinecount = sum(1 for line in open(path_shortfile)) #how many words/lines are in the short and long word files
        longlinecount = sum(1 for line in open(path_longfile))
        while length > 0:
            sorl = random.randint(1,2) #decides to choose long or short word
            if sorl == 1:
                spot = random.randint(1,shortlinecount) # picks line from range of length of file/how many words are in the file
                word = short[spot-1] # grabs the word from the spot
                passwordhard += word.rstrip("\n") # adds to the password
                length -= 1
                answer = wordornum()
                if answer == "number":
                    number = numadder()
                    passwordhard += number
                    gonum -= 1
            else:
                spot = random.randint(1,longlinecount) # same as above process
                word = long[spot-1]
                passwordhard += word.rstrip("\n")
                length -= 1
                answer = wordornum()
                if answer == "number":
                    number = numadder()
                    passwordhard += number
                    gonum -= 1
        while gonum > 0:
            number = numadder()
            passwordhard += number # adds numnber to password at the end
            gonum -= 1
        special = "!$#"
        lap = 2
        while lap > 0:
            spot = random.randint(1,3) # picks a special character
            passwordhard += special[spot-1] # adds SC to password at the end
            lap -= 1
        lf.close()
        sf.close()
        context = {"passwordhard" : ": "+passwordhard} # creates dictionary that is used to place password into HTML
        return render(request, 'passwordgen/hardgen.html', context)
