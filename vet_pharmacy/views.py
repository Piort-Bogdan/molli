from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .permissions import IsStaff
from .serializers import MedicamentSerializer, ManufacturerSerializer

from .models import Medicament, Manufacturer


class MedicamentView(ModelViewSet):
    queryset = Medicament.objects.all()
    model = Medicament
    serializer_class = MedicamentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'price']
    permission_classes = [IsStaff, ]

class ManufacturerView(ModelViewSet):
    queryset = Manufacturer.objects.all()
    model = Manufacturer
    serializer_class = ManufacturerSerializer
    permission_classes = [IsStaff, ]
