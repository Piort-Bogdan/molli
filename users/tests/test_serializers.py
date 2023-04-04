from django.test import TestCase

from users.models import User, Pet
from users.serializers import UserSerializer, PetSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create(password='1232424', username='user1', phone_number='12312312312',
                                          address='test address1', name='full name test1', job_title='DOC',
                                          email='emailtest1@mail.ru', )
        self.user_2 = User.objects.create(password='12324', username='user2', phone_number='1231312',
                                          address='test address2', name='full name test2', job_title='DOC2',
                                          email='emailtest2@mail.ru', )
        self.pet_1 = Pet.objects.create(name='test_pet_name1', year_of_birth='1997-09-09',
                                        species='dog', related_owner_name=self.user_1)
        self.pet_2 = Pet.objects.create(name='test_pet_name2', year_of_birth='1996-09-09',
                                        species='dog2', related_owner_name=self.user_2)

    def test_user_serializer(self):
        serialized_data = UserSerializer([self.user_1, self.user_2], many=True).data

        expected_data = [{
            'id': self.user_1.id,
            'password': '1232424',
            'username': 'user1',
            'phone_number': '12312312312',
            'address': 'test address1',
            'name': 'full name test1',
            'job_title': 'DOC',
            'email': 'emailtest1@mail.ru',
        },
            {
                'id': self.user_2.id,
                'password': '12324',
                'username': 'user2',
                'phone_number': '1231312',
                'address': 'test address2',
                'name': 'full name test2',
                'job_title': 'DOC2',
                'email': 'emailtest2@mail.ru',
            }]

        self.assertEqual(expected_data, serialized_data, serialized_data)

    def test_pet_serializer(self):
        serializers_data = PetSerializer([self.pet_1, self.pet_2], many=True).data

        expected_data = [{
            'name': 'test_pet_name1',
            'year_of_birth': '1997-09-09',
            'species': 'dog',
            'related_owner_name': self.user_1.id
        },
            {
                'name': 'test_pet_name2',
                'year_of_birth': '1996-09-09',
                'species': 'dog2',
                'related_owner_name': self.user_2.id
            }]

        self.assertEqual(serializers_data, expected_data, (serializers_data, expected_data))
