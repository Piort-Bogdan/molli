from rest_framework.viewsets import ModelViewSet

from .models import User, Pet
from .permissions import IsAOwnerAndAuthenticatedOrReadOnly
from .serializers import UserSerializer, PetSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAOwnerAndAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['related_owner_name'] = self.request.user
        serializer.save()