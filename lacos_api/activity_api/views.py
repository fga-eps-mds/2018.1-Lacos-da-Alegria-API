from rest_framework import viewsets

from . import serializers, models


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ActivitySerializer
    queryset = models.Activity.objects.all()
