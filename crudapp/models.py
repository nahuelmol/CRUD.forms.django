from django.db import models

class Contact(models.Model):
    firstName = models.CharField("First name", max_length=255, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=255, blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    
    

class Countries(models.Model):
    Name = models.CharField("Name: ",max_length=255,blank=True,null=True)
    temperature_summer = models.FloatField(default=float)
    temperature_winter = models.IntegerField(default=int)
    
	

