from test_plus.test import TestCase
from ..models import UserProfile


class TestUserProfile(TestCase):

    def test_create_user(self):
        # user1 = self.setUp()
        user1 = UserProfile.objects.create(
            username="ZecaPagodinho",
            password="12345abc",
            email="testeeee@teste.com",
            cpf="246966600",
            name="zecapagodinho",
            birth="2018-04-26",
            region="cataratas",
            preference="deus",
            ddd="11",
            whatsapp="40028922",
            address="casa",
            howDidYouKnow="pericles",
            want_ongs="True",)
        self.assertEqual(user1.username, "ZecaPagodinho")
        self.assertEqual(user1.password, "12345abc")
        self.assertEqual(user1.email, "testeeee@teste.com")
        self.assertEqual(user1.cpf, "246966600")
        self.assertEqual(user1.birth, "2018-04-26")
        self.assertEqual(user1.region, "cataratas")
        self.assertEqual(user1.preference, "deus")
        self.assertEqual(user1.ddd, "11")
        self.assertEqual(user1.whatsapp, "40028922")
        self.assertEqual(user1.address, "casa")
        self.assertEqual(user1.howDidYouKnow, "pericles")
        self.assertEqual(user1.want_ongs, "True")
