from rest_framework import viewsets

from . import serializers, models


class HospitalActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HospitalActivitySerializer
    queryset = models.HospitalActivity.objects.all()


class NGOActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NGOActivitySerializer
    queryset = models.NGOActivity.objects.all()
