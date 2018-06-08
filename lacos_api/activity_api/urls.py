from . import views

urlpatterns = [
    url(r'^activity/$',
        views.ActivityViewSet.as_view(),
        name='activity-set')
]
