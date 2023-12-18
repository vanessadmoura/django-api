from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HelloWorld
from .serializers import HelloWorldSerializer

class HelloWorldView(APIView):
    def get(self, request, format=None):
        hello_world_object = HelloWorld.objects.create(message="Hello, World!")
        serializer = HelloWorldSerializer(hello_world_object)
        return Response(serializer.data, status=status.HTTP_200_OK)