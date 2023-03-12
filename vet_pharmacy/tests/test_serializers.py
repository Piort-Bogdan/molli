from django.test import TestCase

from vet_pharmacy.models import Medicament
from vet_pharmacy.serializers import MedicamentSerializer


class MedicamentSerializerTestCase(TestCase):
    def test_ok(self):
        med1 = Medicament.objects.create(name='test med',
                                         description='test1',
                                         img=None,
                                         count='2',
                                         medicament_form='maz',
                                         article='2',
                                         price='23',
                                         barcode='123123123123'
                                         )
        serializer_data = MedicamentSerializer(med1).data
        print(serializer_data)
        expected_data = {
                'id': med1.id,
                'name': 'test med',
                'description': 'test1',
                'img': None,
                'count': 2,
                'medicament_form': 'maz',
                'article': '2',
                'price': '23.00',
                'barcode': '123123123123',

            }

        self.assertEqual(expected_data, serializer_data)