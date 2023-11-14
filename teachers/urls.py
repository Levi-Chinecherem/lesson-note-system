# teachers/urls.py

from django.urls import path
from .views import (
    dashboard, 
    create_lesson_plan, 
    update_lesson_plan, 
    delete_lesson_plan,
    view_profile,
    update_profile,
    register,
    lesson_plan_detail,
)

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create_lesson_plan/', create_lesson_plan, name='create_lesson_plan'),
    path('update_lesson_plan/<int:lesson_plan_id>/', update_lesson_plan, name='update_lesson_plan'),
    path('delete_lesson_plan/<int:lesson_plan_id>/', delete_lesson_plan, name='delete_lesson_plan'),
    # Example in your urls.py
    path('lesson_plan_detail/<int:pk>/', lesson_plan_detail, name='lesson_plan_detail'),

    
    path('view_profile/', view_profile, name='view_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register/', register, name='register'),
]