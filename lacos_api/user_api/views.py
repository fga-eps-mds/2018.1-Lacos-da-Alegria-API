from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from . import serializers, models
from lacos_api.activity_api.models import HospitalActivity


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'email',)
    @action(methods=['post'], detail=True)
    def delete_user(self, request, pk=None):
        data = request.data
        password = data.get('password')
        user = models.UserProfile.objects.get(pk=pk)
        if user.check_password(password):
            user.delete()
            response = Response({'status': 'Succesfully deleted'}, status.HTTP_200_OK)
        else:
            response = Response({'error': 'Passwords do not match'}, status.HTTP_403_FORBIDDEN)

        return response