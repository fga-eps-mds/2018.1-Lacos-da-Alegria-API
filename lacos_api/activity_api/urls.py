from . import views

app_name = 'activity'

urlpatterns = [
    path(
        '/hospital-activity',
        views.HospitalActivityViewSet.as_view(),
        name='hospital-activity-set'
    )
]
