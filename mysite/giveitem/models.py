from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
import random

class GoList(models.Model):
    list1 = ["goat", "monkey", "hippo"]
    place = random.randint(1,3)
    animal = (list1[place-1])
    print(animal)
    def __str__(self):
        return (self.animal)