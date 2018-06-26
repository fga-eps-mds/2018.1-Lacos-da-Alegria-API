from test_plus.test import TestCase
from rest_framework.test import APIClient
from ..models import News


class TestUserURLs(TestCase):
    """Test Class for Urls tests"""

    def test_create_user_1(self):
        """It should fail creating a user."""
        client = APIClient()
        response = client.post('http://localhost:8000/api/news/', {
            'title': 'Sotexto',
        },
            format='json'
        )
        assert response.status_code == 400

    def test_create_user_2(self):
        """It should create an user."""
        response = self.client.post('http://localhost:8000/api/news/', {
            'title': 'Urgente',
            'text': 'Muita coisa aqui',
            'date_deleted': '2018-07-30T15:30:02-03:00',
        },
            format='json'
        )
        assert response.status_code == 201
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.get().title, 'Urgente')

    def test_detail_user(self):
        """Tests if the user was created"""
        client = APIClient()
        response = client.get('http://localhost:8000/api/news/')
        assert response.status_code == 200
