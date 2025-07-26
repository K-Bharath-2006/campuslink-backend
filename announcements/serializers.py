from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    message = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Announcement(**validated_data).save()
