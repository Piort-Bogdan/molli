from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Appointment, Reception
from .permissions import IsStaff
from .serializers import AppointmentSerializer, ReceptionSerializer


class AppointmentView(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, ]


    def perform_create(self, serializer):
        serializer.validated_data['owner'] == self.request.user
        serializer.save()

class ReceptionView(ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    permission_classes = [IsStaff]

