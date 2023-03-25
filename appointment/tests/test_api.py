import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from appointment.models import Appointment, Reception
from users.models import User, Pet


class AppointmentAPITestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username='user1', phone_number='12312312312', address='test address1',
                                          name='full name test1', password='1232424'
                                          )

        self.pet_1 = Pet.objects.create(name='test_pet1', year_of_birth='1996-09-05', species='dog', owner=self.user_1)

    def test_appointment_create(self):
        url = reverse('appointment-list')
        data = {
            'pet': self.pet_1.id,
            'description': 'test description 1',
            'owner': self.user_1.id,
            'appointment_time': '15:40',
            'appointment_date': '2023-04-06'

        }
        self.client.force_login(self.user_1)
        serialized_data = json.dumps(data)
        response = self.client.post(url, data=serialized_data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(Appointment.objects.all().count(), 1, response.data)
        self.assertEqual(Appointment.objects.get(pet=self.pet_1.id).owner, self.user_1, response.data)

    def test_appointment_update(self):
        pass
    def test_appointment_delete(self):
        pass


class ReceptionAPITestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username='user1', phone_number='12312312312', address='test address1',
                                          name='full name test1', password='1232424', is_staff=True,
                                          )

        self.pet_1 = Pet.objects.create(name='test_pet1', year_of_birth='1996-09-05', species='dog', owner=self.user_1)

        self.reception_test_1 = Reception.objects.create(doctor=self.user_1, owner=self.pet_1.owner,
                                                         pet=self.pet_1, price=15, temperature=39.3,
                                                         preliminary_diagnosis='test diagnosis',
                                                         appointments='test_appointments',
                                                         send_to_email=True,
                                                         recommended_research='Reccomended research test',
                                                         )

    def test_reception_create(self):
        url = reverse('reception-list')
        data = {
            'doctor': self.user_1.id,
            'owner': self.pet_1.owner.id,
            'pet': self.pet_1.id,
            'price': '15.00',
            'temperature': '34.5',
            'preliminary_diagnosis': 'diagnosis',
            'appointments': 'Doctors recomendatoin appointmets',
            'send_to_email': False,
            'recommended_research': 'doctors recomendation researches'

        }

        json_data = json.dumps(data)
        self.client.force_login(self.user_1)
        response = self.client.post(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)

    def test_reception_delete(self):
        url = reverse('reception-detail', args=(self.reception_test_1.id,))
        self.client.force_login(self.user_1)
        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code, response.data)

    def test_reception_update(self):
        url = reverse('reception-detail', args=(self.reception_test_1.id,))
        self.client.force_login(self.user_1)
        data = {
            'temperature': 50.0,
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        self.assertEqual(Reception.objects.get(id=self.reception_test_1.id).temperature, data['temperature'],
                         response.data
                         )
