"""
URL configuration for Notes App project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notes_app.views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
