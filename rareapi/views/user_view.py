"""View module for handling requests about game types"""
from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User


class UserView(ViewSet):
    
    def list(self, request):
        user = request.auth.user
        
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username')
        depth = 1
        
