from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from . import serializers, models
import random

from lacos_api.user_api.models import UserProfile


class HospitalActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HospitalActivitySerializer
    queryset = models.HospitalActivity.objects.all()

    @action(methods=['get'], detail=True)
    def relate_with_activity(self, request, pk=None):
        activity_pk = pk

        user_pk = request.query_params.get('user_key', None)
        try:
            user = UserProfile.objects.get(pk=user_pk)
        except UserProfile.DoesNotExist:
            response = Response({'status': 'Usuário não encontrada!'}, status.HTTP_404_NOT_FOUND)

        monday, tuesday = 0, 1
        allowed_days = [monday, tuesday]
        today = timezone.localdate()
        activity = self.queryset.get(pk=activity_pk)
        activity_time = timezone.localtime(activity.schedule)
        difference = activity.created - timezone.localtime(timezone.now())
        end_activity = activity.schedule + timedelta(minutes=activity.duration)
        response = None

        if activity_pk is not None and today.weekday() in allowed_days:
            try:
                aactivity = models.HospitalActivity.objects.get(pk=pk)
            except models.HospitalActivity.DoesNotExist:
                response = Response({'status': 'Atividade não encontrada!'}, status.HTTP_404_NOT_FOUND)
            
            activitiesid = [activity.id for activity.id in aactivity.preli()]

            if difference > timedelta(hours=2):
                if user.activities.count() != 0:
                    for i in user.activities.all():
                        if (activity.schedule > i.schedule and
                           activity.schedule < (i.schedule + timedelta(minutes=i.duration))):
                            response = Response({'status': 'Conflito de horário com outra atividade '
                                                 'que você está participando!'}, status.HTTP_403_FORBIDDEN)

                        elif end_activity > i.schedule and end_activity < (i.schedule + timedelta(minutes=i.duration)):
                            response = Response({'status': 'Conflito de horário com outra atividade '
                                                 'que você está participando!'}, status.HTTP_403_FORBIDDEN)

                        elif activity.schedule == i.schedule:
                            response = Response({'status': 'Conflito de horário com outra atividade '
                                                 'que você está participando!'}, status.HTTP_403_FORBIDDEN)

                        else:
                            try:
                                prelis.add(user)

                                response = Response({'status': 'Você entrou na pré-lista, '
                                                     'aguarde o resultado do sorteio.'}, status.HTTP_200_OK)
                            except models.User.DoesNotExist:
                                response = Response({'status': 'Atividade não encontrada!'}, status.HTTP_404_NOT_FOUND)
                else:
                    try:
                        prelis.add(user)

                        response = Response({'status': 'Você entrou na pré-lista, '
                                             'aguarde o resultado do sorteio.'}, status.HTTP_200_OK)
                    except models.User.DoesNotExist:

                        response = Response({'status': 'Atividade não encontrada!'}, status.HTTP_404_NOT_FOUND)
            else:
                response = Response({'status': 'Você não pode entrar na pré-lista faltando 2hs '
                                     'ou menos para o início da atividade.'}, status.HTTP_403_FORBIDDEN)

        elif today.weekday() not in allowed_days:
            response = Response({'status': 'Você pode entrar na pré-lista apenas na '
                                 'segunda ou terça-feira.'}, status.HTTP_403_FORBIDDEN)

        else:
            response = Response({'status': 'Missing activity_pk param'}, status.HTTP_400_BAD_REQUEST)

        return response

    
    @action(methods=['get'], detail=True)
    def lottery(self, request, pk=None):
        activity = models.HospitalActivity.objects.get(pk=pk)
        volunteers = [user.id for user in activity.userprofile_set.all()]
        print(volunteers)
        random.shuffle(volunteers)
        sorteados = any
        #lista2 = random.choice(volunteers[0])
        #listaaux = lista2
        for i in volunteers:
            activity.selected = volunteers[0:activity.volunteers]
            fila = volunteers[activity.volunteers:len(volunteers)]
        # print(sorteados)
        print(fila)
        # activity.selected = [1,2,3]
        return Response({'sorteadddosss': activity.selected}, status.HTTP_200_OK)


class NGOActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NGOActivitySerializer
    queryset = models.NGOActivity.objects.all()
