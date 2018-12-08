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


class CommentViewTest(TestCase):
    def test_comment_view_should_render_text_and_comment_form_correctly(self):
        for each in ['positive', 'neutral', 'negative']:
            url = reverse(
                'comment',
                kwargs={
                    'rating': each
                }
            )
            response = self.client.get(url)

            expected = '<h1>Any comment?</h1>'
            self.assertContains(response, expected, status_code=200)

            expected = '<form action="." method="post">'
            self.assertContains(response, expected, status_code=200)

            expected = '<input type="hidden" name="csrfmiddlewaretoken"'
            self.assertContains(response, expected, status_code=200)

            expected = '<textarea name="comment"></textarea>' \
                f'<input type="hidden" name="rating" value="{each}">' \
                '<button type="submit">Submit</button></form>'
            self.assertContains(response, expected, status_code=200)
