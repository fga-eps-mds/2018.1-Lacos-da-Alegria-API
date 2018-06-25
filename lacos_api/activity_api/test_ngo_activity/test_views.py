from django.test import RequestFactory
from ..models import NGOActivity
from rest_framework.test import APIRequestFactory
from test_plus.test import TestCase
from ..views import NGOActivityViewSet

class NGOActivityTestView(TestCase):
    # Should create activity view
    def test_activity_viewset(self):
        request = APIRequestFactory().get("")
        activity_detail = NGOActivityViewSet.as_view({'get': 'retrieve'})
        activity = NGOActivity.objects.create(
            name="hospGama",
            volunteers="30",
            limit=True,
            duration="60",
            call="True",
            schedule="2018-07-30T15:30:02-03:00"
        )
        response = activity_detail(request, pk=activity.pk)
        self.assertEqual(response.status_code, 200)
