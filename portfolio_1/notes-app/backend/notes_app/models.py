from django.db import models
from django.core.exceptions import ValidationError


class Note(models.Model):
    """Model for storing notes"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def clean(self):
        if not self.title.strip():
            raise ValidationError("El título no puede estar vacío")
        if not self.content.strip():
            raise ValidationError("El contenido no puede estar vacío")
