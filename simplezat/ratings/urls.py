from django.urls import path

from .views import CommentView, RatingView

urlpatterns = [
    path('', RatingView.as_view(), name='rating'),
    path('<str:rating>/', CommentView.as_view(), name='comment')
]
