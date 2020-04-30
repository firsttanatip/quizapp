from django.db import models
from django.contrib.auth.models import User, auth
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    

class Exam(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

    

class Questions(models.Model):
   
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(default=timezone.now,null=True)

   

    def __str__(self):
        return self.question


    
    