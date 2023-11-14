# evaluations/forms.py

from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['comment', 'score', 'submission_status']

    submission_status = forms.ChoiceField(choices=(('approved', 'Approved'), ('rejected', 'Rejected')))
