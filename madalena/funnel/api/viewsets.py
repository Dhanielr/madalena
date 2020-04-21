from rest_framework.decorators import action 
from rest_framework import viewsets

from ..models import EntryImages
from .serializers import EntryImagesSerializer

class FunnelViewSet(viewsets.ModelViewSet):

    queryset = EntryImages.objects.all()
    serializer_class = EntryImagesSerializer
    http_method_names = ['post',]