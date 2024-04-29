
from rest_framework.test import APITestCase
from .models import Rick
from django.urls import reverse
from rest_framework import status


class RickTestCase(APITestCase):
    """
        Test for CRUD functionalities for the 'ricks' endpoint
    """

    def test_get_all_ricks(self):
        Rick.objects.create(universe="t380")
        Rick.objects.create(universe="t490")
        response = self.client.get(reverse('ricks-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_one_rick(self):
        new_rick = Rick.objects.create(universe="t380")
        response = self.client.get(reverse('ricks-detail', args=(new_rick.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "id": new_rick.id,
            "universe": new_rick.universee
            })

    def test_get_one_rick_non_existent_id(self):
        response = self.client.get(reverse('ricks-detail', args=(5,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_one_rick(self):
        created_universe = "t590"
        self.assertFalse(Rick.objects.filter(universe=created_universe).exists())
        data = {
            "universe": created_universe
        }
        response = self.client.post(reverse('ricks-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Rick.objects.filter(universe=created_universe).exists())

    def test_create_one_rick_already_existent_universe(self):
        existing_universe = "t590"
        Rick.objects.create(universe=existing_universe)
        data = {
            "universe": existing_universe
        }
        response = self.client.post(reverse('ricks-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_one_rick_no_data(self):
        data = None
        response = self.client.post(reverse('ricks-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_one_rick_missing_universe_data(self):
        data = {
            "universe": ""
        }
        response = self.client.post(reverse('ricks-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_one_rick(self):
        modified_universe = "t390"
        new_rick = Rick.objects.create(universe="t380")
        self.assertFalse(Rick.objects.filter(universe=modified_universe).exists())
        data = {
            "universe": modified_universe
        }
        response = self.client.put(reverse('ricks-detail', args=(new_rick.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Rick.objects.filter(universe=modified_universe).exists())

    def test_update_one_rick_no_data(self):
        new_rick = Rick.objects.create(universe="t380")
        data = None
        response = self.client.put(reverse('ricks-detail', args=(new_rick.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_one_rick_missing_field_data(self):
        new_rick = Rick.objects.create(universe="t380")
        data = {
            "universe": ""
        }
        response = self.client.put(reverse('ricks-detail', args=(new_rick.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_one_rick_non_existent_id(self):
        data = {
            "universe": "t390"
        }
        response = self.client.put(reverse('ricks-detail', args=(5,)), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_one_rick(self):
        checked_universe = "t590"
        new_rick = Rick.objects.create(universe=checked_universe)
        self.assertTrue(Rick.objects.filter(universe=checked_universe).exists())

        response = self.client.delete(reverse('ricks-detail', args=(new_rick.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Rick.objects.filter(universe="t590").exists())

    def test_delete_one_rick_non_existent_id(self):
        response = self.client.delete(reverse('ricks-detail', args=(5,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
