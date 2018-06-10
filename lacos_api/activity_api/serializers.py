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
            'novice',
            'support',
            'limit',
            'created',
            'duration',
            'call',
            'schedule',
            'selected'
        ]


class NGOActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NGOActivity
        fields = [
            'url',
            'id',
            'name',
            'volunteers',
            'limit',
            'created',
            'duration',
            'call'
        ]
