from rest_framework import viewsets

from . import serializers, models


class NewsViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.NewsSerializer
    queryset = models.News.objects.all()
