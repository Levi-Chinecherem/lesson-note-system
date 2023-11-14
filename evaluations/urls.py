# evaluations/urls.py

from django.urls import path
from .views import evaluation_list, evaluate_lesson_plan, delete_evaluation, evaluation_details

app_name = 'evaluations'

urlpatterns = [
    path('list/', evaluation_list, name='evaluation_list'),
    path('evaluate/<int:lesson_plan_id>/', evaluate_lesson_plan, name='evaluate_lesson_plan'),
    path('delete/<int:lesson_plan_id>/', delete_evaluation, name='delete_evaluation'),
    path('details/<int:evaluation_id>/', evaluation_details, name='evaluation_details'),
    # Add more patterns as needed
]
