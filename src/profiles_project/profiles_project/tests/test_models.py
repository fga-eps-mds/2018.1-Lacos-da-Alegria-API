from django.test import TestCase
from ..models import UserProfile

class UserProfileTest (TestCase):
    """ Test model for user profile """
    def setUp (self):
        UserProfile.objects.create(
            name='Renan', login='renan60', email='renanschadt@gmail.com'
        )

    def testLoginUser(self):
        login_renan = UserProfile.objects.get(login='renan60')
        self.assertEqual(
            login_renan.get_email(), "renanschadt@gmail.com pertence a renan60")
