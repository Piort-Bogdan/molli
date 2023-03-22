from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import User, Pet
from .permissions import IsAOwnerAndAuthenticatedOrReadOnly
from .serializers import UserCreateSerializer, PetSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

class PetCreateView(CreateAPIView):
    model = Pet
    serializer_class = PetSerializer
    permission_classes = [IsAOwnerAndAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()