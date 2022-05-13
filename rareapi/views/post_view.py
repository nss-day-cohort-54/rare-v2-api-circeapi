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
from rest_framework.decorators import action
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
        
        
        
    def create(self, request):

        user = Author.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["category"])
        # publication_date = make_aware(datetime.strptime(request.data["publication_date"], '%Y-%m-%d'))

        post = Post()
        post.author = user
        post.title = request.data["title"]
        post.content = request.data["content"]
        post.category = category
        post.image_url = request.data["image_url"]
        post.approved = request.data["approved"]

        try:
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)    
        
    @action(methods=['post', 'delete'], detail=True)
    def tag(self, request, pk):
        """Post and Delete requests to add tags to a post"""
        response_message = ""
        
        post = Post.objects.get(pk=pk)
        tag = request.data['tag']
        
        if request.method == "POST":
            post.tags.add(tag)
            response_message = Response({'message': 'Tag added'}, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            post.tags.remove(tag)
            response_message = Response({'message': 'Tag deleted'}, status=status.HTTP_204_NO_CONTENT)
        
        return response_message

class PostUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


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
        fields = ('id', 'author', 'title', 'content', 'publication_date', 'category', 'image_url', 'approved', 'tags')
        depth = 1
        