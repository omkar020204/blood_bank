from django.db import models
class Login(models.Model):
    username=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=12,default='')
    def __str__(self):
        return self.username
class Form(models.Model):
    address=models.CharField(max_length=100,default='')
    date=models.DateField()
    time=models.TimeField()
    def __str__(self):
        return self.address[:40]

# Create your models here.
