from rest_framework import serializers

from . import models


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.News
        fields = [
            'url',
            'id',
            'title',
            'text',
            'created',
            'date_deleted'
        ]
