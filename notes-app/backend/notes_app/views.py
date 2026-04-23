from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API ViewSet para gestionar notas
    
    Endpoints disponibles:
    - GET /api/notes/ - Obtener todas las notas
    - POST /api/notes/ - Crear una nueva nota
    - GET /api/notes/{id}/ - Obtener una nota por ID
    - PUT /api/notes/{id}/ - Actualizar una nota
    - DELETE /api/notes/{id}/ - Eliminar una nota
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        """Crear una nueva nota con validación"""
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        """Obtener lista de todas las notas"""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Obtener una nota específica por ID"""
        return super().retrieve(request, *args, **kwargs)
