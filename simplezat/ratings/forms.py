from django import forms
from django.forms import ModelForm

from .models import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = [
            'sentiment',
            'comment',
        ]
        widgets = {
            'sentiment': forms.HiddenInput()
        }
