from rest_framework import serializers

from . import models


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = [
            'id',
            'name',
            'volunteers',
            'limit',
            'created',
            'status',
            'time',
            'duration',
            'subscription',
            'call',
            'schedule'
        ]
