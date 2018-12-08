from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class RatingView(TemplateView):
    template_name = 'ratings.html'

    def get(self, request):
        return render(
            request,
            self.template_name
        )


class CommentView(TemplateView):
    template_name = 'comments.html'

    def get(self, request, rating):
        return render(
            request,
            self.template_name,
            {'rating': rating}
        )

    def post(self, request, rating):
        return redirect('thanks')


class ThanksView(TemplateView):
    template_name = 'thanks.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
        )
