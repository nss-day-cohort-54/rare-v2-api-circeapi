"""View module for handling requests about game types"""
from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Author, Photo
from django.contrib.auth.models import User

from rareapi.views.photo import PhotoSerializer 


class AuthorView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single category
        
        Returns:
            Response -- JSON serialized category
        """
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        author = Author.objects.all().order_by('user')
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""
    
    profileImageUrl = serializers.SerializerMethodField()
    def get_profileImageUrl(self, obj):
        photo = PhotoSerializer(Photo.objects.filter(author = obj).last())
        return photo.data
    
    
    
    class Meta:
        model = Author
        fields = ('id', 'user', 'profileImageUrl')
        depth = 1