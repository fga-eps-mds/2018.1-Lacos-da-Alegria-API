from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from lacos_api.user_api.views import UserProfileViewSet
from lacos_api.activity_api.views import HospitalActivityViewSet, NGOActivityViewSet
from lacos_api.news_api.views import NewsViewSet


router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('hospital-activities', HospitalActivityViewSet)
router.register('ngo-activities', NGOActivityViewSet)
router.register('news', NewsViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
