from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ..models import UserProfile
from ..views import UserProfileViewSet
from lacos_api.activity_api.models import NGOActivity
from lacos_api.activity_api.models import HospitalActivity


class UserProfileTestView(TestCase):

    def setUp(self):
        """It should get an user."""
        self.request_factory = APIRequestFactory()
        self.user = UserProfile.objects.create(
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
            want_ongs="True"
        )

        self.ngo = NGOActivity.objects.create(
            name="hospGama",
            volunteers="30",
            duration="60",
            schedule="2018-07-30T15:30:02-03:00"
        )

        self.activity = HospitalActivity.objects.create(
            name="hospGama",
            volunteers="30",
            novice="5",
            duration="60",
            schedule="2018-07-30T15:30:02-03:00"
        )

    def test_user_viewset_Post(self):
        """It should post an user"""
        def setUp(self):
            self.valid_payload = {
                'username': 'ZecaPagodinho',
                'password': '12345abc',
                'email': 'testeeee@teste.com',
                'cpf': '2846966600',
                'name': 'zecapagodinho',
                'birth': '2018-04-26',
                'region': 'cataratas',
                'preference': 'deus',
                'ddd': '61',
                'whatsapp': '40028922',
                'address': 'casa1',
                'howDidYouKnow': 'pericles',
                'want_ongs': 'True',
            }
            self.invalid_payload = {
                'username': '',
                'password': '12345abc',
                'email': 'testeeee@teste.com',
                'cpf': '2846966600',
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

    def test_delete_user(self):
        request = self.request_factory.post('/api/profile/{}/delete_user/'.format(self.user.pk))
        view = UserProfileViewSet.as_view({'post': 'delete_user'})
        response = view(request, pk=self.user.pk)

        print(response.data['error'])
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['error'], 'Passwords do not match')

    def test_get_user_activities(self):
        self.activity.prelist.add(self.user)
        self.activity.save()

        request = self.request_factory.get('/api/profile/{}/get_user_activities/'.format(self.user.pk))
        view = UserProfileViewSet.as_view({'get': 'get_user_activities'})
        response = view(request, pk=self.user.pk)

        mylist = []
        for i in self.user.prelist.all():
            mylist.append(i.pk)

        print(response.data['status'])
        print(response.data['aux'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')
        self.assertEqual(response.data['aux'], mylist)

    def test_get_novice_activities(self):
        self.user.role = "Novato"
        self.user.inscrito = True
        self.user.save()

        self.activity.novice_list = ','.join([str(self.user.pk)])
        self.activity.save()

        request = self.request_factory.get('/api/profile/{}/get_user_activities/'.format(self.user.pk))
        view = UserProfileViewSet.as_view({'get': 'get_user_activities'})
        response = view(request, pk=self.user.pk)

        mylist = []
        novice = []
        novice = [int(n) for n in self.activity.novice_list.split(',')]
        if (self.user.id in novice):
            mylist.append(self.activity.pk)

        print(response.data['status'])
        print(response.data['aux'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')
        self.assertEqual(response.data['aux'], mylist)

    def test_get_user_ngos(self):
        self.ngo.prelistNgo.add(self.user)
        self.ngo.save()

        request = self.request_factory.get('/api/profile/{}/get_user_ngos/'.format(self.user.pk))
        view = UserProfileViewSet.as_view({'get': 'get_user_ngos'})
        response = view(request, pk=self.user.pk)

        mylist = []
        for i in self.user.prelistNgo.all():
            mylist.append(i.pk)

        print(response.data['status'])
        print(response.data['aux'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')
        self.assertEqual(response.data['aux'], mylist)
