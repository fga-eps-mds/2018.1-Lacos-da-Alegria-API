from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from ..user_api import views as userViews
from ..activity_api import views as activityView

router = DefaultRouter()
router.register('profile', userViews.UserProfileViewSet)
router.register('login', userViews.LoginViewSet, base_name='login')
router.register('feed', userViews.UserProfileFeedViewSet)
router.register('activities', activityView.ActivityViewSet)

urlpatterns = [
    url(r'^userprofile-view', userViews.UserProfileView.as_view()),
    url(r'', include(router.urls))
]
