from django.db import models
from django.core.validators import MinLengthValidator


 #Create your models here.
class Name(models.Model):
    wholename = models.CharField(
max_length=200,
            help_text='Enter your whole name')

    def __str__(self):
         return self.name





class Customer(models.Model):
    handle = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_createded = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Week(models.Model):
    weeknum = models.IntegerField(
        help_text='Enter what week you would like to add scores for (between 1-10)',
        max_length=200, null=True )
    name = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.weeknum

class Score(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    week = models.ForeignKey('Week', on_delete=models.CASCADE, null=True)
    movescore = models.BooleanField()
    focusscore = models.BooleanField()
    learnscore = models.BooleanField()

   # def __str__(self):
    #    return self.movescore


