from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


class LettingsModelTest(TestCase):
    def setUp(self):
        address_data = {
          "number": 7217,
          "street": "Bedford Street",
          "city": "Brunswick",
          "state": "GA",
          "zip_code": 31525,
          "country_iso_code": "USA"
        }
        address = Address(**address_data)
        address.save()
        letting_data = {
            "title": "Oceanview Retreat",
            "address_id": address.id
        }
        letting = Letting(**letting_data)
        letting.save()

    def test_address_label(self):
        address = Address.objects.first()
        self.assertIsNotNone(address)
        field_label = address._meta.get_field('number').verbose_name
        self.assertEqual(field_label, 'number')
        field_label = address._meta.get_field('street').verbose_name
        self.assertEqual(field_label, 'street')

    def test_letting_label(self):
        letting = Letting.objects.first()
        field_label = letting._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        field_label = letting._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_url(self):
        letting = Letting.objects.first()
        url = reverse('lettings_index')
        self.assertEqual(url, '/lettings/')
        url = reverse('letting', kwargs={'letting_id' : letting.id})
        self.assertEqual(url, f'/lettings/{letting.id}/')

    def test_letting_index_view(self):
        url = reverse('lettings_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertTrue("lettings_list" in response.context)

    def test_letting_letting_view(self):
        letting = Letting.objects.first()
        url = reverse('letting', kwargs={'letting_id' : letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertTrue("title" in response.context)
        self.assertTrue("address" in response.context)

    def tearDown(self):
        pass
