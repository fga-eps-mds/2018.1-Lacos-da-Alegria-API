from . import views

urlpatterns = [
    url(
        r'^news/$',
        views.NewsViewSet.as_view(),
        name='news-set'
    )
]
