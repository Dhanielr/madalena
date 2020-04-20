from rest_framework import serializers

from ..models import EntryImages

class EntryImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EntryImages
        fields = ('image', 'width', 'height', 'crop')