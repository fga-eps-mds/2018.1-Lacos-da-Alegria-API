from django.test import RequestFactory
from django.urls import reverse
from ..models import UserProfile
from rest_framework.test import APIRequestFactory
from ..views import UserProfileViewSet
from test_plus.test import TestCase


class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


class UserProfileTestView(TestCase):

    def test_user_viewset(self):
        """It should get an user."""
        request = APIRequestFactory().get("")
        user_detail = UserProfileViewSet.as_view({'get': 'retrieve'})
        user = UserProfile.objects.create(username="ZecaPagodinho",
                                          password="12345abc", email="testeeee@teste.com", cpf="246966600",
                                          name="zecapagodinho", birth="2018-04-26", region="cataratas",
                                          preference="deus", ddd="11", whatsapp="40028922", address="casa",
                                          howDidYouKnow="pericles", want_ongs="True")
        response = user_detail(request, pk=user.pk)
        self.assertEqual(response.status_code, 200)

    def test_user_viewset_Post(self):
        """It should post an user"""
        def setUp(self):
            self.valid_payload = {
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
            }
            self.invalid_payload = {
                'username': '',
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
            }

        def test_create_valid_user(self):
            """Call the valid user."""
            response = client.post(
                reverse('post'),
                data=json.dumps(self.valid_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_create_invalid_user(self):
            """Call the invalid user."""
            response = client.post(
                reverse('post'),
                data=json.dumps(self.invalid_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
