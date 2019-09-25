from rest_framework import serializers
from .models import tasks
from rest_framework.validators import UniqueTogetherValidator


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = ('id', 'title', 'is_active', 'is_active', 'is_delete', 'created_at', 'updated_at')
