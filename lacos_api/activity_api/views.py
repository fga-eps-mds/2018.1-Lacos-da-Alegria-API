from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticated

from . import serializers, models, permissions

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ActivitySerializer
    queryset = models.Activity.objects.all()
