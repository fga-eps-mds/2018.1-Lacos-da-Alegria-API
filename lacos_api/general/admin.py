from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Activity)
admin.site.register(models.UserProfile)
