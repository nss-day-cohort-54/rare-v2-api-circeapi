from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.author import Author

from rareapi.models.comment import Comment

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
            Response -- JSON serialized game instance
        """
        author = Author.objects.get(user=request.auth.user)
        
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=author)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # list handles queries
    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        comment = Comment.objects.all()
        # check if string is a query ie /comment?type=1
        game = request.query_params.get('game', None)
        if game is not None:
            comment = comment.filter(game_id=game)
        
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    # added validation 
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        game = Game.objects.get(pk=pk)
        serializer = CreateCommentSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'game', 'gamer')
        depth = 1
        
# validates and saves new game
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'review', 'game']