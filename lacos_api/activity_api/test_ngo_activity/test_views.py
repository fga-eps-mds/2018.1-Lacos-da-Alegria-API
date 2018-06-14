from django.test import RequestFactory
from ..models import NGOActivity
from rest_framework.test import APIRequestFactory
from test_plus.test import TestCase
from ..views import NGOActivityViewSet

# from ..views import (UserRedirectView, UserUpdateView)


class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


class NGOActivityTestView(TestCase):
    # Should create activity view
    def test_activity_viewset(self):
        request = APIRequestFactory().get("")
        activity_detail = NGOActivityViewSet.as_view({'get': 'retrieve'})
        activity = NGOActivity.objects.create(
            name="hospGama",
            volunteers="30",
            limit=True,
            duration="60",
            call="True",
            schedule="2018-07-30T15:30:02-03:00"
        )
        response = activity_detail(request, pk=activity.pk)
        self.assertEqual(response.status_code, 200)

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
