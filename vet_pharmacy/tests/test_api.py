from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from vet_pharmacy.models import Medicament
from vet_pharmacy.serializers import MedicamentSerializer


class MedicamentApiTestCase(APITestCase):
    def setUp(self):
        self.med1 = Medicament.objects.create(name='test med',
                                         price='23',
                                         description='test1',
                                         count='2',
                                         medicament_form='maz',
                                         article='2',
                                         barcode='123123123123'
                                         )
        self.med2 = Medicament.objects.create(name='test med2',
                                         price='223',
                                         description='test2',
                                         count='5',
                                         medicament_form='mdaz',
                                         article='44',
                                         barcode='1231231sdfg123'
                                         )

    def test_get(self):

        url = reverse('medicament')
        response = self.client.get(url)
        serializer_data = MedicamentSerializer([self.med1, self.med2], many=True).data
        self.assertEqual(status.HTTP_200_OK, 200)
        self.assertEqual(serializer_data, response.data)
