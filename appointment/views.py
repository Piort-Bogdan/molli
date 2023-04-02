from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import Pet
from .models import Appointment, Reception
from .permissions import IsStaff, IsAuthenticatedListIsStaffObj
from .serializers import AppointmentSerializer, ReceptionSerializer
from .utilites.send_pdf import create_docx


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
        print(f'это сериализованная инфа {serializer.validated_data}')
        # v_d = serializer.validated_data
        # if v_d['related_owner_name'] is None:
        #     Pet.objects.create(name=v_d['pet'], year_of_birth=v_d['year_of_birth'], species=v_d['species'],
        #                        owner_name=v_d['owner_name'], gender=v_d['gender'], breed=v_d['breed'])
        # create_docx(serializer.validated_data)
        serializer.save()

    # @action(methods=['post'], detail=True, permission_classes=[IsStaff],
    #         url_path='appointments', url_name='appointments')
    # def perform_create(self, serializer, pk=None):
    #     serializer.validated_data['doctor'] == self.request.user
