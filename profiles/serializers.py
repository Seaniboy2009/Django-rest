from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    fields = [
        'id', 'owner', 'created_at', 'updated_at', 'name',
        'content', 'image',
    ]