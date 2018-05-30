from . import views

app_name = 'activity'

urlpatterns = [
    path(
        '/activity',
        views.ActivityViewSet.as_view(),
        name='activity-set'
    )
]
