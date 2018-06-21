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
        activity_pk = pk
        user_pk = request.query_params.get('user_key', None)
        activity = self.queryset.get(pk=activity_pk)
        user = UserProfile.objects.get(pk=user_pk)

        novice_list = []

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
        not_allowed_day = [sunday]
        today = timezone.localdate()
        activity_time = timezone.localtime(activity.schedule)
        difference = activity_time - timezone.localtime(timezone.now())
        end_activity = activity.schedule + timedelta(minutes=activity.duration)

        selected = []
        waiting = []

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
            return Response({'status': 'Succesfully subscribed'}, status.HTTP_200_OK)

        if not(user.id in selected or user.id in waiting) and today.weekday() in subscribe_days:
            waiting.append(user_pk)
            waiting = ', '.join(map(str, waiting))
            activity.waiting = waiting
            activity.save()
            return Response({'status': 'Succesfully subscribed'}, status.HTTP_200_OK)

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
        response = Response({'status': 'User was not subscribed'}, status.HTTP_200_OK)

        novice_list = []

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
                response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)

            elif user.id in waiting:
                waiting.remove(user.id)
                waiting = ', '.join(map(str, waiting))
                activity.waiting = waiting
                activity.save()
                response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)

        if activity.novice_list != "":
            novice_list = [int(n) for n in activity.novice_list.split(',')]
            if user.id in novice_list:
                novice_list.remove(user.id)
                novice_list = ', '.join(map(str, novice_list))
                activity.novice_list = novice_list
                activity.save()
                user.inscrito = False
                user.save()
                response = Response({'status': 'Succesfully deleted from novice queue'}, status.HTTP_200_OK)

        return response

    @action(methods=['get'], detail=True)
    def search_user(self, request, pk=None):
        user_pk = request.query_params.get('user_key', None)
        user = UserProfile.objects.get(pk=user_pk)
        activity = self.queryset.get(pk=pk)

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

    @action(methods=['get'], detail=True)
    def relate_with_ngo(self, request, pk=None):
        activity_pk = pk
        user_pk = request.query_params.get('user_key', None)
        activity = self.queryset.get(pk=activity_pk)

        """# monday, tuesday = 0, 1
        # allowed_days = [monday, tuesday]
        # today = timezone.localdate()
        # activity_time = timezone.localtime(activity.schedule)
        # difference = activity_time - timezone.localtime(timezone.now())
        # end_activity = activity.schedule + timedelta(minutes=activity.duration)"""
        response = Response({'status': 'Succesfully subscribed'}, status.HTTP_200_OK)

        user = UserProfile.objects.get(pk=user_pk)

        activity.prelist.add(user)

        return response

    @action(methods=['get'], detail=True)
    def subscribe(self, request, pk=None):
        activity_pk = pk
        user_pk = request.query_params.get('user_key', None)

        user = UserProfile.objects.get(pk=user_pk)
        activity = self.queryset.get(pk=activity_pk)

        selected = []
        waiting = []

        activity.prelist.add(user)

        """# monday, tuesday = 0, 1
        # allowed_days = [monday, tuesday]
        # today = timezone.localdate()
        # activity_time = timezone.localtime(activity.schedule)
        # difference = activity_time - timezone.localtime(timezone.now())
        # end_activity = activity.schedule + timedelta(minutes=activity.duration)"""
        response = Response({'status': 'User was already subscribed'}, status.HTTP_200_OK)

        if activity.selected != "":
            selected = [int(n) for n in activity.selected.split(',')]

        if activity.waiting != "":
            waiting = [int(n) for n in activity.waiting.split(',')]

        if len(selected) < activity.volunteers and not(user.id in selected or user.id in waiting):
            selected.append(user_pk)
            selected = ', '.join(map(str, selected))
            activity.selected = selected
            activity.save()
            response = Response({'status': 'Succesfully subscribed'}, status.HTTP_200_OK)

        if not(user.id in selected or user.id in waiting):
            waiting.append(user_pk)
            waiting = ', '.join(map(str, waiting))
            activity.waiting = waiting
            activity.save()
            response = Response({'status': 'Succesfully subscribed'}, status.HTTP_200_OK)

        return response

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
        response = Response({'status': 'User was not subscribed'}, status.HTTP_200_OK)

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
                response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)

            if user.id in waiting and waiting != []:
                print('aaaa', user.id)
                waiting.remove(user.id)
                waiting = ', '.join(map(str, waiting))
                activity.waiting = waiting
                activity.save()
                response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)

        return response
