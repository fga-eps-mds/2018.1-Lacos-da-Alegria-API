# from django.urls import reverse, resolve

from test_plus.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from lacos_api.activity_api.models import HospitalActivity


class TestUserURLs(TestCase):
    """Test URL patterns for users app."""

    def setUp(self):
        self.user = self.make_user()


class TestHospitalActivityURLs(APITestCase):

    def test_create_activity_1(self):
        """Ensure we are can't create an activity with invalid fields"""
        client = APIClient()
        response = client.post(
            'http://localhost:8000/api/hospital-activities/',
            {
                'name': 'hospitaln',
                'volunteers': '30'
            },
            format='json'
        )
        assert response.status_code == 400

    def test_create_activity_2(self):
        """Ensure we can create an activity with valid fields"""
        response = self.client.post(
            'http://localhost:8000/api/hospital-activities/',
            {
                'name': 'hospGama',
                'image': 'Imagem',
                'location': 'Rua aleatoria',
                'volunteers': '30',
                'novice': '5',
                'duration': '30',
                'schedule': '2018-07-30T15:30:02-03:00'
            },
            format='json'
        )
        assert response.status_code == 201
        self.assertEqual(HospitalActivity.objects.count(), 1)
        self.assertEqual(HospitalActivity.objects.get().name, 'hospGama')

    def test_detail_activity(self):
        """Ensure we can see the details of each activity"""
        client = APIClient()
        response = client.get('http://localhost:8000/api/hospital-activities/')
        assert response.status_code == 200
