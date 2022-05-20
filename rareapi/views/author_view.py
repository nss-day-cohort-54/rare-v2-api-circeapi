"""View module for handling requests about game types"""
from urllib import request
from django.http import HttpResponseServerError
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Author, Post
from rareapi.views.comment_view import PostSerializer



class AuthorView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single category
        
        Returns:
            Response -- JSON serialized category
        """
        try:
            if pk =='0':
                author = Author.objects.get(author_id=request.auth.user)
            else:
                author = Author.objects.get(pk=pk)
            
            
            # # for post count
            # posts_by_user = Post.objects.filter(author_id=pk)
            Author.objects.annotate(post_count=Count('posts', distinct=True))
            
            # posts_by_user[0].post_count
            
            serializer = AuthorSerializer(author)
            
            # # create a copy of serializer.data
            serializer.data = serializer.data

            # # add a property (w/o modify class, or add a custom property to class)
            # serializer_data["postCount"] = len(posts_by_user)
            
            return Response(serializer.data)
        except Author.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        author = Author.objects.all().order_by('user')
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)
    


class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""
        
    class Meta:
        model = Author
        fields = ('id', 'user', )
        depth = 1
