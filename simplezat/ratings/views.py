from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import RatingForm


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
        initial = {
            'sentiment': rating
        }
        form = RatingForm(initial=initial)

        return render(
            request,
            self.template_name,
            {
                'rating': rating,
                'form': form,
            }
        )

    def post(self, request, rating):
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('thanks')

        return render(
            request,
            self.template_name,
            {
                'rating': rating,
                'form': form
            }
        )


class ThanksView(TemplateView):
    template_name = 'thanks.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
        )
