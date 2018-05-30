from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'user'

urlpatterns = [
    path (
        '/user',
        views.UserProfileViewSet.as_view(),
        name='user'
    )
]

