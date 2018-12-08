from django.test import TestCase
from django.urls import reverse


class RatingViewTest(TestCase):
    def test_rating_view_should_be_accessible(self):
        url = reverse('rating')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
