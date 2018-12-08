from django.test import TestCase
from django.urls import reverse


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('rating')

    def test_rating_view_should_have_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_rating_view_should_show_three_rating_image(self):
        response = self.client.get(self.url)

        expected = '<a href="positive/">' \
            '<img src="/static/images/positive.svg" alt="Positive"></a>'
        self.assertContains(response, expected, status_code=200)

        expected = '<a href="neutral/">' \
            '<img src="/static/images/neutral.svg" alt="Neutral"></a>'
        self.assertContains(response, expected, status_code=200)

        expected = '<a href="negative/">' \
            '<img src="/static/images/negative.svg" alt="Negative"></a>'
        self.assertContains(response, expected, status_code=200)
