from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



from . import serializers, models, permissions
from lacos_api.activity_api.models import Activity


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    @action(methods=['get'], detail=True)
    def relate_with_activity(self, request, pk=None):
        user_pk = pk
        activity_pk = request.query_params.get('activity_key', None)
        activity = Activity.objects.get(pk=activity_pk)

        monday, tuesday = 0, 1
        allowed_days = [monday, tuesday]
        today = timezone.localdate()
        activity_time = timezone.localtime(activity.schedule)
        difference = activity_time - timezone.localtime(timezone.now())
        end_activity = activity.schedule + timedelta(minutes=activity.duration)
        response = None

        if activity_pk is not None and today.weekday() in allowed_days:
            user = self.queryset.get(pk=user_pk)

            if difference > timedelta(hours=2):
                if user.activities.count() != 0:
                    for i in user.activities.all():
                        if (activity.schedule > i.schedule and
                           activity.schedule < (i.schedule + timedelta(minutes=i.duration))):
                            response = Response({'status': 'Clash with other activity'}, status.HTTP_403_FORBIDDEN)

                        elif end_activity > i.schedule and end_activity < (i.schedule + timedelta(minutes=i.duration)):
                            response = Response({'status': 'Clash with other activity'}, status.HTTP_403_FORBIDDEN)

                        elif activity.schedule == i.schedule:
                            response = Response({'status': 'Clash with other activity'}, status.HTTP_403_FORBIDDEN)

                        else:
                            try:
                                user.activities.add(activity)

                                response = Response({'status': 'Created relationship'}, status.HTTP_200_OK)
                            except models.Activity.DoesNotExist:
                                response = Response({'status': 'Activity not found'}, status.HTTP_404_NOT_FOUND)
                else:
                    try:
                        user.activities.add(activity)

                        response = Response({'status': 'Created relationship'}, status.HTTP_200_OK)
                    except models.Activity.DoesNotExist:
                        response = Response({'status': 'Activity not found'}, status.HTTP_404_NOT_FOUND)
            else:
                response = Response({'status': 'Not allowed time'}, status.HTTP_403_FORBIDDEN)

        elif today.weekday() not in allowed_days:
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
