from django.db import models


class HospitalActivity(models.Model):
    name = models.CharField(max_length=60)
    volunteers = models.IntegerField()
    novice = models.IntegerField()
    support = models.IntegerField()
    limit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    call = models.BooleanField(default=False)
    schedule = models.DateTimeField(auto_now_add=False)
    selected = models.IntegerField(blank=True,default=0)

class NGOActivity(models.Model):
    name = models.CharField(max_length=60)
    volunteers = models.IntegerField()
    limit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    call = models.BooleanField(default=False)
