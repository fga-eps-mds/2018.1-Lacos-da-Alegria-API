from test_plus.test import TestCase
from django.db import transaction
from ..models import UserProfile,Activity
import pytest

@pytest.fixture(scope='session')
def generic_user(tmpdir_factory):
    user1 = tmpdir_factory.mktemp('data').UserProfile.objects.create(
        username="ZecaPagodinho",
        password="12345abc",
        email="testeeee@teste.com",
        cpf="246966600",
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
    return user1

class TestUserProfile(TestCase):
    user1 = generic_user(self)
    def test_create_user(self):
        self.assertEqual(user1.username,"ZecaPagodinho")
        self.assertEqual(user1.password,"12345abc")
        self.assertEqual(user1.email,"testeeee@teste.com")
        self.assertEqual(user1.cpf,"246966600")
        self.assertEqual(user1.birth,"2018-04-26")
        self.assertEqual(user1.region,"cataratas")
        self.assertEqual(user1.preference,"deus")
        self.assertEqual(user1.ddd,"11")
        self.assertEqual(user1.whatsapp,"40028922")
        self.assertEqual(user1.address,"casa")
        self.assertEqual(user1.howDidYouKnow,"pericles")
        self.assertEqual(user1.want_ongs,"True")

    def test_get_full_name(self):
        self.assertEqual(self.user1.get_full_name(self), "ZecaPagodinho")
