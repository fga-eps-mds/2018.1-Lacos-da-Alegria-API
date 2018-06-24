from ..models import HospitalActivity
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from lacos_api.activity_api.views import HospitalActivityViewSet
from lacos_api.user_api.models import UserProfile


class HospitalActivityTestView(TestCase):
    def setUp(self):
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
            want_ongs="True",
        )

        self.activity = HospitalActivity.objects.create(
            name="hospGama",
            volunteers="30",
            novice="5",
            support="3",
            limit=True,
            duration="60",
            call="True",
            schedule="2018-07-30T15:30:02-03:00"
        )

    def test_subscribe_novato(self):
        self.user.role = 'Novato'
        self.user.save()

        self.activity.novice_list = ','.join([str(self.user.pk)])
        self.activity.save()
        novice = UserProfile.objects.create(
            username="Pagodinho",
            password="12345abc",
            email="teste@teste.com",
            cpf="246966700",
            name="pagodinho",
            birth="2018-04-26",
            region="cataratas",
            preference="deus",
            ddd="11",
            whatsapp="40028922",
            address="casa",
            howDidYouKnow="pericles",
            want_ongs="True",
        )

        novice.role = 'Novato'
        novice.save()

        request = self.request_factory.get('/api/hospital-activities/{}/subscribe/'.format(self.activity.pk),
                                           {'user_key': novice.pk})
        view = HospitalActivityViewSet.as_view({'get': 'subscribe'})

        response = view(request, pk=self.activity.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Inscrito na fila de novatos')
