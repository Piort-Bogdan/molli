import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from appointment.models import Appointment
from users.models import User, Pet


class AppointmentAPITestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username='user1', phone_number='12312312312', address='test address1',
                                          name='full name test1', password='1232424')

        self.pet_1 = Pet.objects.create(name='test_pet1', year_of_birth='1996-09-05',
                                        species='dog', owner=self.user_1)

    def test_appointment(self):
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

    def test_reception(self):
        url = reverse('appointment-list')
        data = {

        }



