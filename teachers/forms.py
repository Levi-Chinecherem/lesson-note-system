# teachers/forms.py

from django import forms
from .models import LessonPlan,Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['title', 'name', 'email', 'address']
        

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ['subject', 'date', 'plan_details']
        # Add other fields as needed
