# evaluations/models.py

from django.db import models
from django.contrib.auth.models import User
from teachers.models import Title, LessonPlan

class Evaluator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.user.username

class Evaluation(models.Model):
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(Evaluator, on_delete=models.CASCADE, related_name='evaluations')
    comment = models.TextField()
    score = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lesson_plan.subject.title} - {self.evaluator.name} - {self.timestamp}"
