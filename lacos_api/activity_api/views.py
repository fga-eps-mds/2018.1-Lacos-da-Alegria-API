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
    def subscribe(self, request, pk=None):
        """here is received the id of the activity and the user."""
        activity_pk = pk
        user_pk = request.query_params.get('user_key', None)
        activity = self.queryset.get(pk=activity_pk)
        user = UserProfile.objects.get(pk=user_pk)

        novice_list = []

        """enroll the user in the list of novice"""
        if user.role == 'Novato':
            if user.inscrito is False:
                if activity.novice_list != "":
                    novice_list = [int(n) for n in activity.novice_list.split(',')]
                    novice_list.append(user_pk)
                    novice_list = ', '.join(map(str, novice_list))
                    activity.novice_list = novice_list
                    activity.save()
                    user.inscrito = True
                    user.save()
                    return Response({'status': 'Inscrito na fila de novatos'}, status.HTTP_200_OK)
            else:
                return Response({'status': 'Novato já cadastrado em outra atividade'}, status.HTTP_403_FORBIDDEN)

        wednesday, thursday, friday, saturday, sunday = 2, 3, 4, 5, 6
        subscribe_days = [wednesday, thursday, friday, saturday]
        not_allowed_day = sunday
        today = timezone.localdate()
        activity_time = timezone.localtime(activity.schedule)
        difference = activity_time - timezone.localtime(timezone.now())
        end_activity = activity.schedule + timedelta(minutes=activity.duration)

        selected = []
        waiting = []

        """check if less than two hours to activity or check conflict of schedules of activities"""
        if difference < timedelta(hours=2):
            return Response({'status': 'Você não pode entrar na pré-lista faltando 2hs '
                             'ou menos para o início da atividade.'}, status.HTTP_403_FORBIDDEN)

        if user.prelist.count() != 0:
            for i in user.prelist.all():
                if (activity.schedule > i.schedule and
                   activity.schedule < (i.schedule + timedelta(minutes=i.duration))):
                    return Response({'status': 'Conflito de horário com outra atividade '
                                     'que você está participando!'}, status.HTTP_403_FORBIDDEN)

                elif end_activity > i.schedule and end_activity < (i.schedule + timedelta(minutes=i.duration)):
                    return Response({'status': 'Conflito de horário com outra atividade '
                                    'que você está participando!'}, status.HTTP_403_FORBIDDEN)

                elif activity.schedule == i.schedule:
                    return Response({'status': 'Conflito de horário com outra atividade '
                                     'que você está participando!'}, status.HTTP_403_FORBIDDEN)

        """Subscribe user on selected or waiting list"""
        if activity.selected != "":
            selected = [int(n) for n in activity.selected.split(',')]

        if activity.waiting != "":
            waiting = [int(n) for n in activity.waiting.split(',')]

        if today.weekday() is not not_allowed_day and activity_pk is not None:
            activity.prelist.add(user)

        if ((len(selected) < activity.volunteers) and not(user.id in selected or user.id in waiting) and
           (today.weekday() in subscribe_days)):
            selected.append(user_pk)
            selected = ', '.join(map(str, selected))
            activity.selected = selected
            activity.save()
            return Response({'status': 'Selecionado para atividade'}, status.HTTP_200_OK)

        if not(user.id in selected or user.id in waiting) and today.weekday() in subscribe_days:
            waiting.append(user_pk)
            waiting = ', '.join(map(str, waiting))
            activity.waiting = waiting
            activity.save()
            return Response({'status': 'Entrou na fila de espera'}, status.HTTP_200_OK)

        return Response({'status': 'Você entrou na pré-lista, aguarde o resultado do sorteio'}, status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def lottery(self, request, pk=None):
        sorteados = []
        espera = []
        activity = self.queryset.get(pk=pk)
        volunteers = [user.id for user in activity.prelist.all()]
        random.shuffle(volunteers)
        for i in volunteers:
            sorteados = volunteers[0:activity.volunteers]
            espera = volunteers[activity.volunteers:len(volunteers)]

        activity.selected = ''.join(str(sorteados)).strip('[]')
        activity.waiting = ''.join(str(espera)).strip('[]')

        activity.save()

        return Response({'Lottery done succesfully'}, status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def unsubscribe(self, request, pk=None):
        activity_pk = pk
        user_pk = request.query_params.get('user_key', None)

        user = UserProfile.objects.get(pk=user_pk)
        activity = self.queryset.get(pk=activity_pk)
        response = Response({'status': 'Usuário não está inscrito na atividade'}, status.HTTP_405_METHOD_NOT_ALLOWED)

        novice_list = []

        """remove user from prelist and selected or waiting"""
        if user in activity.prelist.all():
            activity.prelist.remove(user)
            selected = []
            waiting = []

            if activity.selected != "":
                selected = [int(n) for n in activity.selected.split(',')]

            if activity.waiting != "":
                waiting = [int(n) for n in activity.waiting.split(',')]

            if user.id in selected:
                selected.remove(user.id)

                if waiting != []:
                    selected.append(waiting[0])
                    waiting.remove(waiting[0])
                    waiting = ', '.join(map(str, waiting))
                    activity.waiting = waiting

                selected = ', '.join(map(str, selected))
                activity.selected = selected
                activity.save()
                response = Response({'status': 'Participação cancelada'}, status.HTTP_200_OK)

            elif user.id in waiting:
                waiting.remove(user.id)
                waiting = ', '.join(map(str, waiting))
                activity.waiting = waiting
                activity.save()
                response = Response({'status': 'Participação cancelada'}, status.HTTP_200_OK)

        """remove user from a novice list"""
        if activity.novice_list != "":
            novice_list = [int(n) for n in activity.novice_list.split(',')]
            if user.id in novice_list:
                novice_list.remove(user.id)
                novice_list = ', '.join(map(str, novice_list))
                activity.novice_list = novice_list
                activity.save()
                user.inscrito = False
                user.save()
                response = Response({'status': 'Participação cancelada'}, status.HTTP_200_OK)

        return response

    @action(methods=['get'], detail=True)
    def search_user(self, request, pk=None):
        user_pk = request.query_params.get('user_key', None)
        user = UserProfile.objects.get(pk=user_pk)
        activity = self.queryset.get(pk=pk)

        """search for user in activity lists"""
        if activity.selected != "":
            selected = [int(n) for n in activity.selected.split(',')]
            if user.id in selected:
                resp = "Sorteado para atividade"
                return Response({'resp': resp}, status.HTTP_200_OK)

        if activity.waiting != "":
            waiting = [int(n) for n in activity.waiting.split(',')]
            if user.id in waiting:
                found = waiting.index(user.id)
                resp = "Na posição " + str(found + 1) + " da fila de espera."
                return Response({'resp': resp}, status.HTTP_200_OK)

        if activity.novice_list != "":
            novice_list = [int(n) for n in activity.novice_list.split(',')]
            if user.id in novice_list:
                found = novice_list.index(user.id)
                resp = "Na posição " + str(found + 1) + " da fila de espera."
                return Response({'resp': resp}, status.HTTP_200_OK)

        else:
            found = "Inscrito na pré-lista"
            response = Response({'resp': found}, status.HTTP_200_OK)

        return response


class NGOActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NGOActivitySerializer
    queryset = models.NGOActivity.objects.all()

    """Objective: this method will enroll the user in ngo activity.
       Parameters: request, pk.
       Returns: it returns a response as status """

    @action(methods=['get'], detail=True)
    def relate_with_ngo(self, request, pk=None):
        ngo_pk = pk
        user_pk = request.query_params.get('user_key', None)
        ngo = self.queryset.get(pk=ngo_pk)
        user = UserProfile.objects.get(pk=user_pk)

        wednesday, thursday, saturday, sunday = 2, 3, 5, 6
        subscribe_days = [wednesday, thursday, saturday]
        not_allowed_day = sunday
        today = timezone.localdate()
        ngo_time = timezone.localtime(ngo.schedule)
        difference = ngo_time - timezone.localtime(timezone.now())
        end_ngo = ngo.schedule + timedelta(minutes=ngo.duration)

        selected = []
        waiting = []

        if difference < timedelta(hours=2):
            return Response({'status': 'Você não pode entrar na pré-lista faltando 2hs '
                             'ou menos para o início da atividade.'}, status.HTTP_403_FORBIDDEN)

        if user.prelistNgo.count() != 0:
            for i in user.prelistNgo.all():
                if (ngo.schedule > i.schedule and
                   ngo.schedule < (i.schedule + timedelta(minutes=i.duration))):
                    return Response({'status': 'Conflito de horário com outra atividade '
                                     'que você está participando!'}, status.HTTP_403_FORBIDDEN)

                elif end_ngo > i.schedule and end_ngo < (i.schedule + timedelta(minutes=i.duration)):
                    return Response({'status': 'Conflito de horário com outra atividade '
                                    'que você está participando!'}, status.HTTP_403_FORBIDDEN)

                elif ngo.schedule == i.schedule:
                    return Response({'status': 'Conflito de horário com outra atividade '
                                     'que você está participando!'}, status.HTTP_403_FORBIDDEN)

        """Subscribe user on selected or waiting list"""
        if ngo.selected != "":
            selected = [int(n) for n in ngo.selected.split(',')]

        if ngo.waiting != "":
            waiting = [int(n) for n in ngo.waiting.split(',')]

        if today.weekday() is not not_allowed_day and ngo_pk is not None:
            ngo.prelistNgo.add(user)

        if ((len(selected) < ngo.volunteers) and not(user.id in selected or user.id in waiting) and
           (today.weekday() in subscribe_days)):
            selected.append(user_pk)
            selected = ', '.join(map(str, selected))
            ngo.selected = selected
            ngo.save()
            return Response({'status': 'Selecionado para a atividade'}, status.HTTP_200_OK)

        if not(user.id in selected or user.id in waiting) and today.weekday() in subscribe_days:
            waiting.append(user_pk)
            waiting = ', '.join(map(str, waiting))
            ngo.waiting = waiting
            ngo.save()
            return Response({'status': 'Entrou na fila de espera'}, status.HTTP_200_OK)

        return Response({'status': 'Você entrou na pré-lista, aguarde o resultado do sorteio'}, status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def lottery(self, request, pk=None):
        sorteados = []
        espera = []
        ngo = self.queryset.get(pk=pk)
        volunteers = [user.id for user in ngo.prelistNgo.all()]
        random.shuffle(volunteers)
        for i in volunteers:
            sorteados = volunteers[0:ngo.volunteers]
            espera = volunteers[ngo.volunteers:len(volunteers)]

        ngo.selected = ''.join(str(sorteados)).strip('[]')
        ngo.waiting = ''.join(str(espera)).strip('[]')

        ngo.save()

        return Response({'Lottery done succesfully'}, status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def unsubscribe(self, request, pk=None):
        ngo_pk = pk
        user_pk = request.query_params.get('user_key', None)

        user = UserProfile.objects.get(pk=user_pk)
        ngo = self.queryset.get(pk=ngo_pk)
        response = Response({'status': 'Usuário não está inscrito na atividade'}, status.HTTP_405_METHOD_NOT_ALLOWED)

        if user in ngo.prelistNgo.all():
            ngo.prelistNgo.remove(user)
            selected = []
            waiting = []

            if ngo.selected != "":
                selected = [int(n) for n in ngo.selected.split(',')]

            if ngo.waiting != "":
                waiting = [int(n) for n in ngo.waiting.split(',')]

            if user.id in selected:
                selected.remove(user.id)

                if waiting != []:
                    selected.append(waiting[0])
                    waiting.remove(waiting[0])
                    waiting = ', '.join(map(str, waiting))
                    ngo.waiting = waiting

                selected = ', '.join(map(str, selected))
                ngo.selected = selected
                response = Response({'status': 'Participação cancelada'}, status.HTTP_200_OK)

            elif user.id in waiting:
                waiting.remove(user.id)
                waiting = ', '.join(map(str, waiting))
                ngo.waiting = waiting
                response = Response({'status': 'Participação cancelada'}, status.HTTP_200_OK)

            ngo.save()

        return response

    @action(methods=['get'], detail=True)
    def search_user_ngo(self, request, pk=None):
        user_pk = request.query_params.get('user_key', None)
        user = UserProfile.objects.get(pk=user_pk)
        ngo = self.queryset.get(pk=pk)
        response = Response({'Erro'}, status.HTTP_403_FORBIDDEN)

        if ngo.selected != "":
            selected = [int(n) for n in ngo.selected.split(',')]
            if user.id in selected:
                found = "Sorteado para atividade"
                return Response({'resp': found}, status.HTTP_200_OK)

        if ngo.waiting != "":
            waiting = [int(n) for n in ngo.waiting.split(',')]
            if user.id in waiting:
                found = waiting.index(user.id)
                resp = "Na posição " + str(found + 1) + " da fila de espera."
                return Response({'resp': resp}, status.HTTP_200_OK)

        else:
            found = "Inscrito na pré-lista"
            response = Response({'resp': found}, status.HTTP_200_OK)

        return response
