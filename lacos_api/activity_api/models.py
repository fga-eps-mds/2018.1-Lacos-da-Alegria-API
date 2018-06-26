from django.db import models


class HospitalActivity(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    volunteers = models.IntegerField()
    novice = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    schedule = models.DateTimeField(auto_now_add=False)
    novice_list = models.CharField(max_length=10000, default='', blank=True)
    prelist = models.ManyToManyField('user_api.UserProfile', blank=True, related_name='prelist')
    selected = models.CharField(max_length=10000, default='', blank=True)
    waiting = models.CharField(max_length=10000, default='', blank=True)


class NGOActivity(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    volunteers = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    schedule = models.DateTimeField(auto_now_add=False)
    prelistNgo = models.ManyToManyField('user_api.UserProfile', blank=True, related_name='prelistNgo')
    selected = models.CharField(max_length=10000, default='')
    waiting = models.CharField(max_length=10000, default='')
