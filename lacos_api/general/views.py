import datetime
from rest_framework import  filters, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    @action(methods=['get'], detail=True)
    def relate_with_activity(self, request, pk=None):
        user_pk = pk
        activity_pk = request.query_params.get('activity_key', None)

        monday, tuesday = 5, 6
        allowed_days = [monday, tuesday]
        today = datetime.date.today()

        response = None
        if activity_pk is not None and today in allowed_days:
            user = self.queryset.get(pk=user_pk)

            try:
                activity = models.Activity.objects.get(pk=activity_pk)
                user.activities.add(activity)

                response = Response({'status': 'Created relationship'}, status.HTTP_200_OK)
            except models.Activity.DoesNotExist:
                response = Response({'status': 'Activity not found'}, status.HTTP_404_NOT_FOUND)
        elif today not in allowed_days:
            response = Response({'status': 'Not allowed date'}, status.HTTP_403_FORBIDDEN)

        else:
            response = Response({'status': 'Missing activity_pk param'}, status.HTTP_400_BAD_REQUEST)

        return response


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ActivitySerializer
    queryset = models.Activity.objects.all()
