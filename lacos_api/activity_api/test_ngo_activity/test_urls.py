# from django.urls import reverse, resolve

from test_plus.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from ..models import NGOActivity


class TestUserURLs(TestCase):
    """Test URL patterns for users app."""

    def setUp(self):
        self.user = self.make_user()


class TestNGOActivityURLs(APITestCase):

    def test_create_activity_1(self):
        """Ensure we are can't create an activity with invalid fields"""
        client = APIClient()
        response = client.post(
            'http://localhost:8000/api/ngo-activities/',
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
            'http://localhost:8000/api/ngo-activities/',
            {
                'name': 'hospGama',
                'location': 'qualquer coisa',
                'image': 'ibages',
                'volunteers': '30',
                'duration': '30',
                'schedule': '2018-07-30T15:30:02-03:00'
            },
            format='json'
        )
        assert response.status_code == 201
        self.assertEqual(NGOActivity.objects.count(), 1)
        self.assertEqual(NGOActivity.objects.get().name, 'hospGama')

    def test_detail_activity(self):
        """Ensure we can see the details of each activity"""
        client = APIClient()
        response = client.get('http://localhost:8000/api/ngo-activities/')
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
