from rest_framework import serializers

from . import models


class HospitalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HospitalActivity
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


class NGOActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NGOActivity
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
