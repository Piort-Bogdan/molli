from django.test   import TestCase

from users.models import User
from users.serializers import UserSerializer


class UserSerializerTestCase(TestCase):

    def test_user_serializer(self):
        self.user_1 = User.objects.create(password='1232424', username='user1', phone_number='12312312312', address='test address1',
                                          name='full name test1',  job_title='DOC')
        self.user_2 = User.objects.create(username='user2', phone_number='8767', address='test address2',
                                          name='full name test2', password='123wasd24', job_title= 'DOC2')

        serialized_data = UserSerializer([self.user_1, self.user_2], many=True).data

        expected_data = [{
            'id': self.user_1.id,
            'password': '1232424',
            'username': 'user1',
            'job_title': 'DOC',
            'name': 'full name test1',
            'phone_number': '12312312312',
            'address': 'test address1'
        },
        {
            'id': self.user_2.id,
            'password': '123wasd24',
            'username': 'user2',
            'job_title': 'DOC2',
            'name': 'full name test2',
            'phone_number': '8767',
            'address': 'test address2',
        }]

        self.assertEqual(expected_data, serialized_data, serialized_data)
