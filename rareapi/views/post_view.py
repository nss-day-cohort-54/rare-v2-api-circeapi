from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.functions import Coalesce
from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from datetime import datetime
from rareapi.models import Post, Author, Category

class PostView(ViewSet):
    
    def list(self, request):

        user_id = self.request.query_params.get("user_id", None)

        if user_id == None : 
            posts = Post.objects.all().order_by('-publication_date')
            
        else :    
            posts = Post.objects.filter(
                Q(author = user_id)).order_by('-publication_date')
                
        

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
        

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'label')        

        
class PostSerializer(serializers.ModelSerializer):
    
    author = PostAuthorSerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'publication_date', 'category')
        