from rest_framework import serializers
from snippet.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'email', 'title', 'content', 'created']