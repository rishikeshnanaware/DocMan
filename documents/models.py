from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

# documents/serializers.py
from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
