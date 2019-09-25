from rest_framework import serializers
from .models import notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = notes
        fields = ('id', 'title', 'is_active', 'is_active', 'is_delete', 'created_at', 'updated_at')
