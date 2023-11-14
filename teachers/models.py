# teachers/models.py

from django.db import models
from django.contrib.auth.models import User

class Title(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class PlanDetails(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class LessonPlan(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    SUBMISSION_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
    ]

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    plan_details = models.ForeignKey(PlanDetails, on_delete=models.CASCADE)
    submission_status = models.CharField(
        max_length=20,
        choices=SUBMISSION_STATUS_CHOICES,
        default=PENDING,
    )
    
