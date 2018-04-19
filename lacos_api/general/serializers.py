from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)
    address = serializers.CharField(min_length=3)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = (
            'id',
            'email',
            'name',
            'password',
            'address',
            'username',
            'cpf',
            'birth',
            'region',
            'preference',
            'howDidYouKnow',
            'want_ongs',
            'ddd',
            'whatsapp',
            'genre'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
            address=validated_data['address'],
            username=validated_data['username'],
            cpf=validated_data['cpf'],
            birth=validated_data['birth'],
            region=validated_data['region'],
            preference=validated_data['preference'],
            howDidYouKnow=validated_data['howDidYouKnow'],
            want_ongs=validated_data['want_ongs'],
            ddd=validated_data['ddd'],
            whatsapp=validated_data['whatsapp'],
            genre=validated_data['genre']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


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
            'call'
        ]
