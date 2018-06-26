from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from lacos_api.activity_api.views import NGOActivityViewSet
from lacos_api.user_api.models import UserProfile
from ..models import NGOActivity


class NGOActivityTestView(TestCase):
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

        self.ngo = NGOActivity.objects.create(
            name="hospGama",
            volunteers="30",
            duration="60",
            schedule="2018-07-30T15:30:02-03:00"
        )

    def test_subscribe(self):
        self.user.role = 'Voluntario'
        self.user.save()

        request = self.request_factory.get('/api/hospital-activities/{}/relate_with_ngo/'.format(self.ngo.pk),
                                           {'user_key': self.user.pk})
        view = NGOActivityViewSet.as_view({'get': 'relate_with_ngo'})
        response = view(request, pk=self.ngo.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Você entrou na pré-lista, aguarde o resultado do sorteio')

        ngo2 = NGOActivity.objects.create(
            name="hospGama",
            volunteers="30",
            duration="60",
            schedule="2018-07-30T15:30:02-03:00"
        )

        response = view(request, pk=ngo2.pk)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Conflito de horário com outra atividade '
                         'que você está participando!')

        ngo2.schedule = "2018-07-30T15:02:00-03:00"
        ngo2.save()

        response = view(request, pk=ngo2.pk)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Conflito de horário com outra atividade '
                         'que você está participando!')

        ngo2.schedule = "2018-07-30T16:02:00-03:00"
        ngo2.save()

        response = view(request, pk=ngo2.pk)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Conflito de horário com outra atividade '
                         'que você está participando!')

        ngo2.schedule = "2018-06-25T12:00:02-03:00"
        ngo2.save()

        response = view(request, pk=ngo2.pk)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['status'], 'Você não pode entrar na pré-lista faltando 2hs '
                         'ou menos para o início da atividade.')

    def test_unsubscribe(self):
        request = self.request_factory.get('/api/ngo-activities/{}/unsubscribe/'.format(self.ngo.pk),
                                           {'user_key': self.user.pk})
        view = NGOActivityViewSet.as_view({'get': 'unsubscribe'})
        response = view(request, pk=self.ngo.pk)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['status'], 'Usuário não está inscrito na atividade')

        self.ngo.prelistNgo.add(self.user)
        self.ngo.waiting = ','.join([str(self.user.pk)])
        self.ngo.save()

        response = view(request, pk=self.ngo.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Participação cancelada')

        self.ngo.prelistNgo.add(self.user)
        self.ngo.selected = ','.join([str(self.user.pk)])
        self.ngo.save()

        response = view(request, pk=self.ngo.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Participação cancelada')

    def test_search_user(self):
        self.ngo.selected = ','.join([str(self.user.pk)])
        self.ngo.save()

        request = self.request_factory.get('/api/hospital-activities/{}/search_user_ngo/'.format(self.ngo.pk),
                                           {'user_key': self.user.pk})
        view = NGOActivityViewSet.as_view({'get': 'search_user_ngo'})
        response = view(request, pk=self.ngo.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['resp'], 'Sorteado para atividade')

    def test_search_user_waiting(self):
        self.ngo.waiting = ','.join([str(self.user.pk)])
        self.ngo.save()

        request = self.request_factory.get('/api/hospital-activities/{}/search_user_ngo/'.format(self.ngo.pk),
                                           {'user_key': self.user.pk})
        view = NGOActivityViewSet.as_view({'get': 'search_user_ngo'})

        response = view(request, pk=self.ngo.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['resp'], 'Na posição 1 da fila de espera.')

    def test_search_user_prelist(self):
        self.ngo.prelistNgo.add(self.user.pk)
        self.ngo.save()

        request = self.request_factory.get('/api/hospital-activities/{}/search_user_ngo/'.format(self.ngo.pk),
                                           {'user_key': self.user.pk})
        view = NGOActivityViewSet.as_view({'get': 'search_user_ngo'})
        response = view(request, pk=self.ngo.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['resp'], 'Inscrito na pré-lista')
