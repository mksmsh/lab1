from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Person


class PersonAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person = Person.objects.create(
            name="John Doe",
            age=30,
            address="123 Main St",
            work="Software Engineer"
        )
        self.valid_payload = {
            "name": "Jane Doe",
            "age": 25,
            "address": "456 Elm St",
            "work": "Data Scientist"
        }
        self.invalid_payload = {
            "name": "",
            "age": -10,
            "address": "",
            "work": ""
        }

    def test_get_all_persons(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_person(self):
        response = self.client.get(reverse('person_detail', kwargs={'person_id': self.person.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.person.name)

    def test_create_valid_person(self):
        response = self.client.post(reverse('person_list'), data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_person(self):
        response = self.client.post(reverse('person_list'), data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_person(self):
        response = self.client.delete(reverse('person_detail', kwargs={'person_id': self.person.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
