from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserSerializer
# Create your views here.


class ProfileUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer