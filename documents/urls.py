from django.urls import path
from .views import UploadDocument

urlpatterns = [
    path('upload/', UploadDocument.as_view(), name='upload'),
]
