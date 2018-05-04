# from django.urls import reverse, resolve

from test_plus.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from ..models import Activity


class TestUserURLs(TestCase):
    """Test URL patterns for users app."""

    def setUp(self):
        self.user = self.make_user()


class TestActivityURLs(APITestCase):

    def test_create_activity_1(self):
        """Ensure we are can't create an activity with invalid fields"""
        client = APIClient()
        response = client.post(
            'http://localhost:8000/api/activities/',
            {
                'name': 'hospGama',
                'volunteers': '30'
            },
            format='json'
        )
        assert response.status_code == 400

    def test_create_activity_2(self):
        """Ensure we can create an activity with valid fields"""
        response = self.client.post(
            'http://localhost:8000/api/activities/',
            {
                'name': 'hospGama',
                'volunteers': '30',
                'limit': 'True',
                'status': '1',
                'duration': '30',
                'subscription': 'True',
                'call': 'True'
            },
            format='json'
        )
        assert response.status_code == 201
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(Activity.objects.get().name, 'hospGama')

    def test_detail_activity(self):
        """Ensure we can see the details of each activity"""
        client = APIClient()
        response = client.get('http://localhost:8000/api/activities/')
        assert response.status_code == 200

    def test_user_login(self):
        """Ensure we can lo gin with the username and password of an existent user"""
        response = self.client.post(
            'http://localhost:8000/api/profile/',
            {
                'username': 'ZecaPagodinho',
                'password': '12345abc',
                'email': 'testeeee@teste.com',
                'cpf': '246966600',
                'name': 'zecapagodinho',
                'birth': '2018-04-26',
                'region': 'cataratas',
                'preference': 'deus',
                'ddd': '11',
                'whatsapp': '40028922',
                'address': 'casa',
                'howDidYouKnow': 'pericles',
                'want_ongs': 'True',
                'genre': 'M'
            },
            format='json'
        )
        assert response.status_code == 201

        response = self.client.post(
            'http://localhost:8000/api/token/',
            {
                'username': 'ZecaPagodinho',
                'password': '12345abc',
            },
            format='json'
        )
        assert response.status_code == 200

    def test_user_login_2(self):
        """Ensure we can't log in with the username and the wrong password of a user"""
        response = self.client.post(
            'http://localhost:8000/api/profile/',
            {
                'username': 'ZecaPagodinho',
                'password': '12345abc',
                'email': 'testeeee@teste.com',
                'cpf': '246966600',
                'name': 'zecapagodinho',
                'birth': '2018-04-26',
                'region': 'cataratas',
                'preference': 'deus',
                'ddd': '11',
                'whatsapp': '40028922',
                'address': 'casa',
                'howDidYouKnow': 'pericles',
                'want_ongs': 'True',
                'genre': 'M'
            },
            format='json'
        )
        assert response.status_code == 201

        response = self.client.post(
            'http://localhost:8000/api/token/',
            {
                'username': 'ZecaPagodinho',
                'password': '12345abcdefg',
            },
            format='json'
        )
        assert response.status_code == 400

    # def test_list_reverse(self):
    #     """users:list should reverse to /users/."""
    #     self.assertEqual(reverse("users:list"), "/users/")

    # def test_list_resolve(self):
    #     """/users/ should resolve to users:list."""
    #     self.assertEqual(resolve("/users/").view_name, "users:list")

    # def test_redirect_reverse(self):
    #     """users:redirect should reverse to /users/~redirect/."""
    #     self.assertEqual(reverse("users:redirect"), "/users/~redirect/")

    # def test_redirect_resolve(self):
    #     """/users/~redirect/ should resolve to users:redirect."""
    #     self.assertEqual(resolve("/users/~redirect/").view_name, "users:redirect")

    # def test_detail_reverse(self):
    #     """users:detail should reverse to /users/testuser/."""
    #     self.assertEqual(
    #         reverse("users:detail", kwargs={"username": "testuser"}), "/users/testuser/"
    #     )

    # def test_detail_resolve(self):
    #     """/users/testuser/ should resolve to users:detail."""
    #     self.assertEqual(resolve("/users/testuser/").view_name, "users:detail")

    # def test_update_reverse(self):
    #     """users:update should reverse to /users/~update/."""
    #     self.assertEqual(reverse("users:update"), "/users/~update/")

    # def test_update_resolve(self):
    #     """/users/~update/ should resolve to users:update."""
    #     self.assertEqual(resolve("/users/~update/").view_name, "users:update")
