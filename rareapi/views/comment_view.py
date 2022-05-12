from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.author import Author

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
        

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_on', 'author_id', 'post_id', 'subject')
# validates and saves new game
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'post', 'subject']