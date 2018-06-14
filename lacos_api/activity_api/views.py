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
        activity = self.queryset.get(pk=activity_pk)

        monday, tuesday = 0, 1
        allowed_days = [monday, tuesday]
        today = timezone.localdate()
        activity_time = timezone.localtime(activity.schedule)
        difference = activity_time - timezone.localtime(timezone.now())
        end_activity = activity.schedule + timedelta(minutes=activity.duration)
        response = Response({'status': 'Succesfully subscribed'}, status.HTTP_200_OK)
        
        user = UserProfile.objects.get(pk=user_pk)
        
        activity.prelist.add(user)

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

        return Response({'Lottery succesfully done'}, status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def unsubscribe(self,request, pk=None):
        activity_pk = pk
        user_pk = request.query_params.get('user_key', None)

        user = UserProfile.objects.get(pk=user_pk)
        activity = self.queryset.get(pk=activity_pk)
        response = Response({'status': 'User was not subscribed'}, status.HTTP_404_NOT_FOUND)

        if user in activity.prelist.all():
            activity.prelist.remove(user)
            response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)
            
        if activity.selected == '':
            return response
            
        selected = [int(n) for n in activity.selected.split(',')]

        if user.id in selected:
            selected.remove(user.id)
            print(selected)
            selected = ', '.join(map(str, selected))
            activity.selected = selected
            activity.save()
            response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)
        
        else:
            waiting = [int(n) for n in activity.waiting.split(',')]
            waiting.remove(user.id)
            waiting = ', '.join(map(str, waiting))
            activity.waiting = waiting
            activity.save()
            response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)

        return response


class NGOActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NGOActivitySerializer
    queryset = models.NGOActivity.objects.all()
