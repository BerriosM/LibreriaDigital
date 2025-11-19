from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book_title', 'rating', 'text']
        widgets = {
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
