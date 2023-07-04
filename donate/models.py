from django.db import models
class Donor(models.Model):
    name=models.CharField(max_length=30,default='')
    dob=models.DateField()
    aadhar=models.CharField(max_length=12)
    bloodGrp=models.CharField(max_length=3,default='')
    donationDate=models.DateField()
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    def __str__(self):
        return self.name
class Donor2(models.Model):
    name=models.CharField(max_length=30,default='')
    dob=models.DateField()
    aadhar=models.CharField(max_length=12)
    bloodGrp=models.CharField(max_length=3,default='')
    donationDate=models.DateField()
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    def __str__(self):
        return self.name