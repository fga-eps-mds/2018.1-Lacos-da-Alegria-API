from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers, models
import random


class HospitalActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HospitalActivitySerializer
    queryset = models.HospitalActivity.objects.all()

    @action(methods=['get'], detail=True)
    def sort(self, request, pk=None):
        activity = models.HospitalActivity.objects.get(pk=pk)
        volunteers = [user.id for user in activity.userprofile_set.all()]
        print(volunteers)
        random.shuffle(volunteers)
        #lista2 = random.choice(volunteers[0])
        #listaaux = lista2
        for i in volunteers:
            lista =  volunteers[0:3]
        print(lista)
        return Response({'oi': str(lista)}, status.HTTP_200_OK)


class NGOActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NGOActivitySerializer
    queryset = models.NGOActivity.objects.all()
