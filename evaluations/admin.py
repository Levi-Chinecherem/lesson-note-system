# evaluations/admin.py

from django.contrib import admin
from .models import Evaluator, Evaluation

@admin.register(Evaluator)
class EvaluatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'name')
    search_fields = ('user__username', 'name')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('lesson_plan', 'evaluator', 'comment', 'score', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('lesson_plan__subject__title', 'evaluator__user__username')
