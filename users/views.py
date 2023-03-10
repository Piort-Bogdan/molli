from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import User, Pet
from .serializers import UserCreateSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

