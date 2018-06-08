from rest_framework import serializers

from . import models


class HospitalActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HospitalActivity
        fields = [
            'url',
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


class NGOActivitySerializer(serializers.HyperlinkedModelSerializer):
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
            'call'
        ]
