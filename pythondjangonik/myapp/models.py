from django.db import models
 
class Person(models.Model):
    Login = models.CharField(max_length=30)
    Password = models.CharField(max_length=50)
