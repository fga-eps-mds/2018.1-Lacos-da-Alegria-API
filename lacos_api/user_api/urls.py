from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'user'

urlpatterns = [
    path (
        '/user-feed',
        views.UserProfileFeedViewSet.as_view(),
        name='user-feed'
    )
    path (
        '/user-view',
        views.UserProfileView.as_view(),
        name='user-view'
    )
    path (
        '/user-view-set',
        views.UserProfileViewSet.as_view(),
        name='user-view-set'
    )
]

