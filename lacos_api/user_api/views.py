from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from . import serializers, models

from lacos_api.activity_api.models import HospitalActivity


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

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

    @action(methods=['post'], detail=True)
    def edit_user(self, request, pk=None):
        data = request.data
        password = data.get('password')
        user = models.UserProfile.objects.get(pk=pk)
        if user.check_password(password):
            response = Response({'error': 'A senha nova coincide com a senha antiga'}, status.HTTP_403_FORBIDDEN)
        else:
            user.set_password(password)
            user.save()
            print(user)
            response = Response({'password': user.password}, status.HTTP_200_OK)

        return response

    @action(methods=['get'], detail=True)
    def get_user_activities(self, request, pk=None):
        user = models.UserProfile.objects.get(pk=pk)
        activities = HospitalActivity.objects.all()
        mylist = []
        novice = []
        if (user.inscrito is True and user.role == "Novato"):
            for i in activities:
                novice = [int(n) for n in i.novice_list.split(',')]
                if (user.id in novice):
                    mylist.append(i.pk)
                    return Response({'status': 'ok', 'aux': mylist}, status.HTTP_200_OK)

        aux = user.prelist.all()
        print(aux)
        for i in aux:
            mylist.append(i.pk)

        response = Response({'status': 'ok', 'aux': mylist}, status.HTTP_200_OK)
        return response

    @action(methods=['get'], detail=True)
    def get_user_ngos(self, request, pk=None):
        user = models.UserProfile.objects.get(pk=pk)
        mylist = []

        aux = user.prelistNgo.all()
        print(aux)
        for i in aux:
            mylist.append(i.pk)
        response = Response({'status': 'ok', 'aux': mylist}, status.HTTP_200_OK)
        return response
