from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Student registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

class StudentLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if not user.is_student:
                return Response({"error": "Not a student"}, status=403)
            token = RefreshToken.for_user(user)
            return Response({
                'refresh': str(token),
                'access': str(token.access_token),
                'username': user.username,
            })
        return Response(serializer.errors, status=400)

class AdminLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if not user.is_admin:
                return Response({"error": "Not an admin"}, status=403)
            token = RefreshToken.for_user(user)
            return Response({
                'refresh': str(token),
                'access': str(token.access_token),
                'username': user.username,
            })
        return Response(serializer.errors, status=400)
