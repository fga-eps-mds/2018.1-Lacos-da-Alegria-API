from ..models import HospitalActivity
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from lacos_api.activity_api.views import HospitalActivityViewSet
from lacos_api.user_api.models import UserProfile
from django.utils import timezone


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

        activity2 = HospitalActivity.objects.create(
            name="hospGama",
            volunteers="30",
            novice="5",
            support="3",
            limit=True,
            duration="60",
            call="True",
            schedule="2018-07-30T15:30:02-03:00"
        )

        request = self.request_factory.get('/api/hospital-activities/{}/subscribe/'.format(self.activity.pk),
                                           {'user_key': novice.pk})
        view = HospitalActivityViewSet.as_view({'get': 'subscribe'})
        response = view(request, pk=self.activity.pk)
        print(response.data['status'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['status'], 'Inscrito na fila de novatos')

        request = self.request_factory.get('/api/hospital-activities/{}/subscribe/'.format(activity2.pk),
                                           {'user_key': novice.pk})
        response = view(request, pk=activity2.pk)
        print(response.data['status'])
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Novato já cadastrado em outra atividade')

    def test_pre_list(self):
        self.user.role = 'Voluntario'
        self.user.save()

        request = self.request_factory.get('/api/hospital-activities/{}/subscribe/'.format(self.activity.pk),
                                           {'user_key': self.user.pk})
        view = HospitalActivityViewSet.as_view({'get': 'subscribe'})
        response = view(request, pk=self.activity.pk)
        print(response.data['status'])


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Você entrou na pré-lista, aguarde o resultado do sorteio')

        activity2 = HospitalActivity.objects.create(
            name="hospGama",
            volunteers="30",
            novice="5",
            support="3",
            limit=True,
            duration="60",
            call="True",
            schedule="2018-07-30T15:30:02-03:00"
        )

        response = view(request, pk=activity2.pk)
        print(response.data['status'])

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Conflito de horário com outra atividade '
                        'que você está participando!')

        activity2.schedule = "2018-07-30T15:02:00-03:00"
        activity2.save()

        response = view(request, pk=activity2.pk)
        print(response.data['status'])
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Conflito de horário com outra atividade '
                'que você está participando!')

        activity2.schedule = "2018-07-30T16:02:00-03:00"
        activity2.save()

        response = view(request, pk=activity2.pk)
        print(response.data['status'])
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Conflito de horário com outra atividade '
                'que você está participando!')

        activity2.schedule = "2018-06-25T12:00:02-03:00"
        activity2.save()

        response = view(request, pk=activity2.pk)
        print(response.data['status'])

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Você não pode entrar na pré-lista faltando 2hs '
                         'ou menos para o início da atividade.')
