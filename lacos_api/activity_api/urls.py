from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'activity'

urlpatterns = [
    path (
        '/activity',
        views.ActivityViewSet.as_view(),
        name='activity-set'
    )
]
