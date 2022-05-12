"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

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
        categories = Category.objects.all()
        
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
    
class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for Categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')