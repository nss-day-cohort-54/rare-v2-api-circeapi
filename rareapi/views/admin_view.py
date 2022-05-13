"""View module for handling requests about game types"""
from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.admin import Admin



class AdminView(ViewSet):
    
    def list(self, request):
        admin = Admin.objects.all()
        
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

class AdminSerializer(serializers.ModelSerializer):
    """JSON serializer for admin"""
    class Meta:
        model = Admin
        fields = ('id', 'user')