from rest_framework import serializers

from . import models


class HospitalActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HospitalActivity
        fields = [
            'url',
            'id',
            'name',
            'novice',
            'image',
            'location',
            'volunteers',
            'created',
            'duration',
            'schedule',
            'novice_list',
            'prelist',
            'selected',
            'waiting'
        ]


class NGOActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NGOActivity
        fields = [
            'url',
            'id',
            'name',
            'image',
            'location',
            'volunteers',
            'created',
            'duration',
            'schedule',
            'prelistNgo',
            'selected',
            'waiting'
        ]
