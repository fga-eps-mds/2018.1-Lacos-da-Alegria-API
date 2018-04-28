# from django.urls import reverse, resolve

from test_plus.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models import UserProfile


class TestUserURLs(TestCase):
    """Test URL patterns for users app."""

    def test_create_user_1(self):
        client = APIClient()
        response = client.post('http://localhost:8000/api/profile/',
            {
                'name' : 'ZecaPagodinho',
            },
            format='json'
        )
        assert response.status_code == 400

    def test_create_user_2(self):
        client = APIClient()
        response = self.client.post('http://localhost:8000/api/profile/',
            {    
                'username':'ZecaPagodinho',
                'password':'12345abc',
                'email':'testeeee@teste.com',
                'cpf':'246966600',
                'name':'zecapagodinho',
                'birth': '2018-04-26',
                'region':'cataratas',
                'preference':'deus',
                'ddd':'11',
                'whatsapp':'40028922',
                'address':'casa',
                'howDidYouKnow':'pericles',
                'want_ongs':'True',
                'genre' : 'M'
            },
            format='json'
        )
        assert response.status_code == 201
        self.assertEqual(UserProfile.objects.count(),1)
        self.assertEqual(UserProfile.objects.get().username,'ZecaPagodinho')

    def test_detail_user(self):
        client = APIClient()
        response = client.get('http://localhost:8000/api/profile/')
        assert response.status_code == 200
















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
