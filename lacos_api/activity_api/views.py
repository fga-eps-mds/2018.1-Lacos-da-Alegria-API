from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers, models
import random


class HospitalActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HospitalActivitySerializer
    queryset = models.HospitalActivity.objects.all()

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
            fila = volunteers[activity.volunteers+1:len(volunteers)]
        # print(sorteados)
        # activity.selected = [1,2,3]
        return Response({'sorteadddosss': activity.selected}, status.HTTP_200_OK)


class NGOActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NGOActivitySerializer
    queryset = models.NGOActivity.objects.all()
