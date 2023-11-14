# evaluations/forms.py
from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['comment', 'score', 'submission_status']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'}),
            'submission_status': forms.Select(attrs={'class': 'form-control'}),
        }

    submission_status = forms.ChoiceField(choices=(('approved', 'Approved'), ('rejected', 'Rejected')), widget=forms.Select(attrs={'class': 'form-control'}))
