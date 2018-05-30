from . import views

app_name = 'user'

urlpatterns = [
    path(
        '/user',
        views.UserProfileViewSet.as_view(),
        name='user'
    )
]
