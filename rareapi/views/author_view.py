"""View module for handling requests about game types"""
from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Author


class AuthorView(ViewSet):
    
    def list(self, request):
        author = Author.objects.all().order_by('-user')
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""
    class Meta:
        model = Author
        fields = ('id', 'user')
        depth = 1