from django.test import TestCase
from django.urls import reverse


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('rating')

    def test_rating_view_should_have_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)
