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
    novice_list = models.CharField(max_length=10000, default='')
    prelist = models.ManyToManyField('user_api.UserProfile', blank=True, related_name='prelist')
    selected = models.CharField(max_length=10000, default='')
    waiting = models.CharField(max_length=10000, default='')


class NGOActivity(models.Model):
    name = models.CharField(max_length=60)
    volunteers = models.IntegerField()
    limit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    call = models.BooleanField(default=False)
    schedule = models.DateTimeField(auto_now_add=False)
    prelist = models.ManyToManyField('user_api.UserProfile', blank=True, related_name='prelistNgo')
    selected = models.CharField(max_length=10000, default='')
    waiting = models.CharField(max_length=10000, default='')
