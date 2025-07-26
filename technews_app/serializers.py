from rest_framework import serializers
from .models import TechNews

class TechNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechNews
        fields = ['id', 'title', 'description', 'application_link', 'created_at']
        read_only_fields = ['id', 'created_at']
