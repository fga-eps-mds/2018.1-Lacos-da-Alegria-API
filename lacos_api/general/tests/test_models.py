from test_plus.test import TestCase
from ..models import UserProfile,Activity
from django.db import models

class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()

    # def test__str__(self):
    #     self.assertEqual(
    #         self.user.__str__(),
    #         "testuser",  # This is the default username for self.make_user()
    #     )

    # def test_get_absolute_url(self):
    #     self.assertEqual(self.user.get_absolute_url(), "/profiles/testuser/")
   
class TestUserProfile(TestCase):
    def setUp(self):
        return UserProfile.objects.create(
            username="ZecaPagodinho",
            password="ClaytuRasta",
            email="teste@teste.com",
            cpf="2469666",
            name="zecapagodinho",
            birth= "2018-04-26",
            region="cataratas",
            preference="deus",
            ddd="11",
            whatsapp="40028922",
            address="casa",
            howDidYouKnow="pericles",
            want_ongs="True"
       )
    def test_create_user(self):
        user_test = self.setUp()
        self.assertEqual(user_test.username,"ZecaPagodinho")
        self.assertEqual(user_test.password,"ClaytuRasta")
        self.assertEqual(user_test.email,"teste@teste.com")
        self.assertEqual(user_test.cpf,"2469666")
        self.assertEqual(user_test.birth,"2018-04-26")
        self.assertEqual(user_test.region,"cataratas")
        self.assertEqual(user_test.preference,"deus")
        self.assertEqual(user_test.ddd,"11")
        self.assertEqual(user_test.whatsapp,"40028922")
        self.assertEqual(user_test.address,"casa")
        self.assertEqual(user_test.howDidYouKnow,"pericles")
        self.assertEqual(user_test.want_ongs,"True")