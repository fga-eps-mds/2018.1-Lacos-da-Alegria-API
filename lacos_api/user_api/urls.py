from . import views

urlpatterns = [
    url(
        r'^user/$',
        views.UserProfileViewSet.as_view(),
        name='user-set'
    )
]
