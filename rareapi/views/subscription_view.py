"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.author import Author

from rareapi.models.subscription import Subscription
from django.db.models import Q
class SubscriptionView(ViewSet):
    """Rater app Subscription view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single subscription
        
        Returns:
            Response -- JSON serialized subscription
        """
        try:
            subscription = Subscription.objects.get(pk=pk)
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data)
        except Subscription.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all subs
        
        Returns:
            Response -- JSON serialized list of subs
        """
        follower = self.request.query_params.get("follower", None)
        if follower is not None:
            subscriptions = Subscription.objects.filter(
                    Q(follower = follower) 
            )
        else:
            subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        Returns
            response -- JSON serialized subscription instance"""
            
        follower = Author.objects.get(user=request.auth.user)
        serializer = CreateSubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(follower=follower)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        subscription = Subscription.objects.get(pk=pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        subscription = Subscription.objects.get(pk=pk)
        subscription.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for Subs"""
    class Meta:
        model = Subscription
        fields = ('id', 'author', 'follower', 'created_on')
        
class CreateSubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for Subs"""
    class Meta:
        model = Subscription
        fields = ('author',)