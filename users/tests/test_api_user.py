import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User, Pet


class UserApiTestCase(APITestCase):

    def setUp(self):
        self.user_1 = User.objects.create(username='user1', phone_number='12312312312', address='test address1',
                                          name='full name test1', password='123adfgdfg2424')
        self.pet_1 = Pet.objects.create(name='user2s pet', year_of_birth='1997-03-03',
                                        species='dog', related_owner_name=self.user_1)

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'user2',
            'email': 'user1@email.ru',
            'password': '123adfgdfg2424',
            'phone_number': '6876876',
            'address': 'Address Test',
            'name': 'Lobanov Aleksey Kurilev'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(User.objects.all().count(), 2, response.data)

    def test_create_pet(self):
        url = reverse('pet-list')
        data = {
            'name': 'user1s pet',
            'year_of_birth': '1997-03-03',
            'species': 'dog',
            'related_owner_name': self.user_1.id
        }
        # self.client.force_login(self.user_1)
        self.client.force_authenticate(self.user_1)
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(Pet.objects.filter(related_owner_name=self.user_1.id).last().related_owner_name.id, self.user_1.id, response.data)

    def test_pet_delete(self):
        url = reverse('pet-detail', args=(self.pet_1.id,))
        # self.client.force_login(self.user_1)
        self.client.force_authenticate(self.user_1)

        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code, response.data)

    def test_pet_update(self):
        url = reverse('pet-detail', args=(self.pet_1.id,))
        # self.client.force_login(self.user_1)
        self.client.force_authenticate(self.user_1)
        data = {
            'species': 'cat'
        }
        data_json = json.dumps(data)
        response = self.client.patch(url, data=data_json, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        self.assertEqual(Pet.objects.get(id=self.pet_1.id).species, data['species'], response.data)
