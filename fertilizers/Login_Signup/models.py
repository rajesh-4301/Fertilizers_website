from django.db import models
from django.contrib.auth.models import User

class login_info(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)

class signup_info(models.Model):  
    id = models.AutoField(primary_key=True)  # Explicit primary key
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)  # Prevent duplicate emails
    password = models.CharField(max_length=128)  # Store hashed password for security
    cpassword = models.CharField(max_length=128)  # Store hashed password for security
    
    def __str__(self):
        return self.fullname
