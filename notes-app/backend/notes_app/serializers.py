from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("El título no puede estar vacío")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("El contenido no puede estar vacío")
        return value
