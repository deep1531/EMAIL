from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .emails import *
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterAPI(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()  # Save the user if the data is valid
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
            
            # Handle invalid data
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Handle unexpected errors and return the error response
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

