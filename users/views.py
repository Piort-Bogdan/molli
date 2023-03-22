from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import User, Pet
from .permissions import IsAOwnerAndAuthenticatedOrReadOnly
from .serializers import UserCreateSerializer, PetSerializer


class UserCreateView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class PetCreateView(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAOwnerAndAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()