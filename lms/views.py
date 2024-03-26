from django.contrib.auth import authenticate
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Assignment, Question, Class
from .serializers import UserSerializer, AssignmentSerializer, QuestionSerializer, ClassSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer

def api_documentation(request):
    return render(request, 'base.html')

# Users
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Assignments
class AssignmentListView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

# Questions
class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Classes
class ClassListView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class UserAuthenticationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            # Authentication successful
            return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
