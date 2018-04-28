from django.test import RequestFactory
from django.urls import reverse
from ..models import UserProfile
from rest_framework.test import APIRequestFactory
from ..urls import urlpatterns
from ..views import UserProfileViewSet
from test_plus.test import TestCase

# from ..views import (UserRedirectView, UserUpdateView)


class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()

class UserProfileTestView(TestCase):
    def test_user_viewset(self):
        request = APIRequestFactory().get("")
        user_detail = UserProfileViewSet.as_view({'get': 'retrieve'})
        user = UserProfile.objects.create(username = "ZecaPagodinho",password="12345abc",email="testeeee@teste.com",
                                          cpf="246966600",name="zecapagodinho",birth= "2018-04-26",region="cataratas",
                                          preference="deus",ddd="11",whatsapp="40028922",address="casa",
                                          howDidYouKnow="pericles",want_ongs="True")
        response = user_detail(request, pk=user.pk)
        self.assertEqual(response.status_code,200)


    def test_user_viewset_Post(self):
        def setUp(self):
            self.valid_payload = {
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
                'want_ongs':'True'
            }
            self.invalid_payload = {
                'username':'',
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
                    'want_ongs':'True'
            }
        def test_create_valid_user(self):
            response = client.post(
                reverse('post'),
                data=json.dumps(self.valid_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_create_invalid_user(self):
            response = client.post(
                reverse('post'),
                data=json.dumps(self.invalid_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
            

























# class TestUserRedirectView(BaseUserTestCase):

#     def test_get_redirect_url(self):
#         # Instantiate the view directly. Never do this outside a test!
#         view = UserRedirectView()
#         # Generate a fake request
#         request = self.factory.get("/fake-url")
#         # Attach the user to the request
#         request.user = self.user
#         # Attach the request to the view
#         view.request = request
#         # Expect: '/users/testuser/', as that is the default username for
#         #   self.make_user()
#         self.assertEqual(view.get_redirect_url(), "/users/testuser/")


# class TestUserUpdateView(BaseUserTestCase):

#     def setUp(self):
#         # call BaseUserTestCase.setUp()
#         super(TestUserUpdateView, self).setUp()
#         # Instantiate the view directly. Never do this outside a test!
#         self.view = UserUpdateView()
#         # Generate a fake request
#         request = self.factory.get("/fake-url")
#         # Attach the user to the request
#         request.user = self.user
#         # Attach the request to the view
#         self.view.request = request

#     def test_get_success_url(self):
#         # Expect: '/users/testuser/', as that is the default username for
#         #   self.make_user()
#         self.assertEqual(self.view.get_success_url(), "/users/testuser/")

#     def test_get_object(self):
#         # Expect: self.user, as that is the request's user object
#         self.assertEqual(self.view.get_object(), self.user)
