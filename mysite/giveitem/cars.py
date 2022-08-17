import re
import os.path
from os.path import exists
import random

def car():
    file = open("carlist.txt")
    cars = file.readlines()
    spot = random.randint(1,8)
    car = cars[spot-1]
    mobile = {car : spot}
    return mobile