import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User, Pet
from users.serializers import UserCreateSerializer


class UserApiTestCase(APITestCase):

    def setUp(self):

        self.user_1 = User.objects.create(username='user1', phone_number='12312312312', address='test address1',
                                               name='full name test1', password='1232424')

    def test_create_user(self):
        url = reverse('create-user')
        data = {
            'username': 'user2',
            'email': 'user1@email.ru',
            'password': '123',
            'phone_number': '6876876',
            'address': 'Address Test',
            'name': 'Lobanov Aleksey Kurilev'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(User.objects.all().count(), 2, response.data)

    def test_create_pet(self):
        url = reverse('create-pet')
        data = {
            'name': 'user1s pet',
            'year_of_birth': '1997-03-03',
            'species': 'dog',
            'owner': self.user_1.id
        }
        self.client.force_login(self.user_1)
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(Pet.objects.get(owner=self.user_1.id).id, self.user_1.id, response.data )





