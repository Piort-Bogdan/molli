from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Appointment, Reception
from .permissions import IsStaff, IsAuthenticatedListIsStaffObj
from .serializers import AppointmentSerializer, ReceptionSerializer
from .utilites.send_pdf import create_word_and_convert_to_pdf


class AppointmentView(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticatedListIsStaffObj, ]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] == self.request.user
        serializer.save()


class ReceptionView(ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    # permission_classes = [IsStaff]



    def perform_create(self, serializer):
        serializer.validated_data['doctor'] == self.request.user
        serializer.save()


