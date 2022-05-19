from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.author import Author
from django.contrib.auth.models import User
from rareapi.models.comment import Comment
from rareapi.models.post import Post


class CommentView(ViewSet):
    """Level up game comments"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    # create a new comment
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized comment instance
        """
        author = Author.objects.get(user=request.auth.user)
        comment = Comment.objects.create(
            subject = request.data['subject'],
            content = request.data['content'],
            author = author,
            post_id = request.data['post_id']
        )
        serializer = CreateCommentSerializer(comment)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # list handles queries
    def list(self, request):
        comments = Comment.objects.all()
        post = request.query_params.get('post', None)
        if post is not None:
            comments = comments.filter(post_id=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    # added validation 
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        comment = Comment.objects.get(pk=pk)
        serializer = CreateCommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class AuthorSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False)
    class Meta:
        model = Author
        fields = ['id', 'user']

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    author = AuthorSerializer(many=False)
    
    class Meta:
        
        model = Comment
        fields = ('id', 'content', 'created_on', 'author', 'subject', 'post')
        depth = 2
# validates and saves new game
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'post', 'subject', 'created_on']
        
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'category', 'publication_date', 'image_url', 'content', 'approved', 'comments')        