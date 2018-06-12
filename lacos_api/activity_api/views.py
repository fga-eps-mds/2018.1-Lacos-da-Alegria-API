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
        response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)
        
        user = UserProfile.objects.get(pk=user_pk)
        
        activity.prelis.add(user)

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
