from django.conf.urls import url, include

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
