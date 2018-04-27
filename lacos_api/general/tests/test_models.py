from test_plus.test import TestCase
from django.db import transaction
from ..models import UserProfile,Activity
#from django.db import models

# class TestUser(TestCase):
#
#     def setUp(self):
#         self.user = self.make_user()

    # def test__str__(self):
    #     self.assertEqual(
    #         self.user.__str__(),
    #         "testuser",  # This is the default username for self.make_user()
    #     )

    # def test_get_absolute_url(self):
    #     self.assertEqual(self.user.get_absolute_url(), "/profiles/testuser/")

class TestUserProfile(TestCase):
    # def test_constraint(self):
    #     try:
    #         # Duplicates should be prevented.
    #         with transaction.atomic():
    #             UserProfile.objects.create(
    #                 username="ZecaPagodinho",
    #                 password="abc12345",
    #                 email="testeeee@teste.com",
    #                 cpf="2469666",
    #                 name="zecapagodinho",
    #                 birth= "2018-04-26",
    #                 region="cataratas",
    #                 preference="deus",
    #                 ddd="11",
    #                 whatsapp="40028922",
    #                 address="casa",
    #                 howDidYouKnow="pericles",
    #                 want_ongs="True"
    #                 )
    #             self.fail('Duplicate question allowed.')
    #     except IntegrityError:
    #             pass
    # def setUp(self):
    #     with transaction.atomic():
    #         return UserProfile.objects.create(
    #             username="ZecaPagodinho",
    #             password="abc12345",
    #             email="testeeee@teste.com",
    #         #    cpf="246966600",
    #             name="zecapagodinho",
    #             birth= "2018-04-26",
    #             region="cataratas",
    #             preference="deus",
    #             ddd="11",
    #             whatsapp="40028922",
    #             address="casa",
    #             howDidYouKnow="pericles",
    #             want_ongs="True"
    #        )
    def test_create_user(self):
        # user1 = self.setUp()
        user1 = UserProfile.objects.create(
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
