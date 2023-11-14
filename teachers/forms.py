# teachers/forms.py

from django import forms
from .models import LessonPlan,Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['title', 'name', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ['subject', 'date', 'plan_details']
        widgets = {
           'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'plan_details': forms.Textarea(attrs={'class': 'form-control'}),
        }