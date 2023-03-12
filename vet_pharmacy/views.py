import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from .serializers import MedicamentSerializer, ManufacturerSerializer

from .models import Medicament, Manufacturer, Pharmacy


class MedicamentAddView(ListCreateAPIView):
    queryset = Medicament.objects.all()
    model = Medicament
    serializer_class = MedicamentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'price']


class ManufacturerAddView(ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    model = Manufacturer
    serializer_class = ManufacturerSerializer
