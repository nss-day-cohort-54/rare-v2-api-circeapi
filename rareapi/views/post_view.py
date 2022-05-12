from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from datetime import datetime
from rareapi.models import Post, Author

class PostView(ViewSet):
    
    def list(self, request):

        posts = Post.objects.all()
        user = Author.objects.get(user=request.auth.user)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):

        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        

class PostUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PostAuthorSerializer(serializers.ModelSerializer):

    user = PostUserSerializer(many=False)
    class Meta:
        model = Author
        fields = ['id', 'user']

        
class PostSerializer(serializers.ModelSerializer):
    
    user = PostAuthorSerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'publication_date')
        