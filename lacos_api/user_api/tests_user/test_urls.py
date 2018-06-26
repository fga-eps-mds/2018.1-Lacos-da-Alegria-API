from test_plus.test import TestCase
from rest_framework.test import APIClient
from ..models import UserProfile


class TestUserURLs(TestCase):
    """Test Class for Urls tests"""

    def test_create_user_1(self):
        """It should fail creating a user."""
        client = APIClient()
        response = client.post('http://localhost:8000/api/profile/', {
            'name': 'ZecaPagodinho',
        },
            format='json'
        )
        assert response.status_code == 400

    def test_create_user_2(self):
        """It should create an user."""
        response = self.client.post('http://localhost:8000/api/profile/', {
            'username': 'ZecaPagodinho',
            'password': '12345abc',
            'email': 'testeeee@teste.com',
            'cpf': '24696660080',
            'name': 'zecapagodinho',
            'birth': '2018-04-26',
            'region': 'Águas Claras',
            'preference': 'Hospital Regional do Gama',
            'ddd': '61',
            'whatsapp': '40028922',
            'address': 'casa1',
            'howDidYouKnow': 'Outros',
            'want_ongs': 'True',
            'genre': 'Masculino',
            'role': 'Novato',
        },
            format='json'
        )
        assert response.status_code == 201
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().username, 'ZecaPagodinho')

    def test_detail_user(self):
        """Tests if the user was created"""
        client = APIClient()
        response = client.get('http://localhost:8000/api/profile/')
        assert response.status_code == 200
