from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from ..user_api import views as userViews
from ..activity_api import views as activityView

router = DefaultRouter()
router.register('profile', userViews.UserProfileViewSet)
router.register('login', userViews.LoginViewSet, base_name='login')
router.register('activities', activityView.ActivityViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
