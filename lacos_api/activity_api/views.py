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
        sorteados = []
        espera = []        
        activity = self.queryset.get(pk=pk)
        volunteers = [user.id for user in activity.prelis.all()]
        random.shuffle(volunteers)
        for i in volunteers:
            sorteados = volunteers[0:activity.volunteers]
            espera = volunteers[activity.volunteers:len(volunteers)]
        activity.selected = ''.join(str(sorteados))
        activity.waiting = ''.join(str(espera))
        print("aqui",activity.selected)
        # activity.selected = [1,2,3]
        return Response({'sorteadddosss': activity.waiting}, status.HTTP_200_OK)


class NGOActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NGOActivitySerializer
    queryset = models.NGOActivity.objects.all()
