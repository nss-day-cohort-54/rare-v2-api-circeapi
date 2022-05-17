"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category
from django.db.models import Q
class CategoryView(ViewSet):
    """Rater app Category view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single category
        
        Returns:
            Response -- JSON serialized category
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all categories
        
        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all().order_by('label')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        Returns
            response -- JSON serialized category instance"""
            
        
        category = Category.objects.create(
            label = request.data['label']
        )
        
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for Categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')