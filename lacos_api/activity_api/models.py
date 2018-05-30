from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Activity(models.Model):
    
    name = models.CharField(max_length=60)
    volunteers = models.IntegerField()
    limit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    subscription = models.BooleanField(default=False)
    call = models.BooleanField(default=False)
    schedule = models.DateTimeField(auto_now_add=False)