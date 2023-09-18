from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    answer_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter answer.', 'style': 'width: 100%;height:200px; border-radius:10px;','class':'form-control'}))
    class Meta:
        model = Answer
        fields = ['answer_text']
