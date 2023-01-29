from django.db import models

class Citizen(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    Status = models.TextField() 
    Salary = models.IntegerField()

class Workers(models.Model):
    name = models.ForeignKey(Citizen, on_delete = models.PROTECT)
    worker = models.TextField() 
   

