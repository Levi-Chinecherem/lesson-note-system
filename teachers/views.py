# teachers/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, LessonPlan, Subject, PlanDetails
from .forms import LessonPlanForm
from django.contrib.auth.decorators import login_required
from .forms import TeacherForm
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.db import models

@login_required
def view_profile(request):
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'teachers/view_profile.html', {'teacher': teacher})

@login_required
def update_profile(request):
    teacher = Teacher.objects.get(user=request.user)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers:view_profile')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/update_profile.html', {'form': form})


def register(request):
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            user = request.user
            try:
                # Attempt to get the teacher for the user
                existing_teacher = Teacher.objects.get(user=user)
                # If the user already has a teacher profile, inform the user
                message = "You have already registered. You cannot register twice."
                return render(request, 'message_template.html', {'message': message})

            except Teacher.DoesNotExist:
                # If the user doesn't have a teacher profile, proceed with registration
                teacher = teacher_form.save(commit=False)
                teacher.user = user
                teacher.save()
                messages.success(request, 'Registration successful!')
                return redirect('teachers:view_profile')
    else:
        teacher_form = TeacherForm()

    return render(request, 'teachers/register.html', {'teacher_form': teacher_form})

def lesson_plan_detail(request, pk):
    lesson_plan = get_object_or_404(LessonPlan, pk=pk)

    # You can add more context variables or customize the logic as needed
    context = {'lesson_plan': lesson_plan}

    return render(request, 'teachers/lesson_plan_detail.html', context)
    
@login_required
def dashboard(request):
    try:
        # Try to get the Teacher instance
        teacher = Teacher.objects.get(user=request.user)
        subjects = Subject.objects.filter(lessonplan__teacher=teacher)
    except Teacher.DoesNotExist:
        # If Teacher instance does not exist, display a message
        message = "Welcome! Please fill in your profile details to get started."
        return render(request, 'message_template.html', {'message': message})

    # Fetch approved and pending lesson plans
    approved_lesson_plans = LessonPlan.objects.filter(teacher=teacher, submission_status='approved')
    pending_lesson_plans = LessonPlan.objects.filter(teacher=teacher, submission_status='pending')

    # Chart data
    total_lesson_plans = LessonPlan.objects.filter(teacher=teacher).count()
    total_pending_plans = pending_lesson_plans.count()
    total_approved_plans = approved_lesson_plans.count()

    # Number of subjects to lesson plans
    subjects_with_plans = Subject.objects.filter(lessonplan__teacher=teacher).annotate(num_plans=models.Count('lessonplan'))


    # Number of teachers to one subject
    subjects_with_teachers = Subject.objects.annotate(num_teachers=Count('lessonplan', distinct=True))
    subject_names_teachers = [subject.title for subject in subjects_with_teachers]
    num_teachers = [subject.num_teachers for subject in subjects_with_teachers]

    # Subject with highest and lowest number of plans
    subject_with_highest_plans = subjects_with_plans.order_by('-num_plans').first()
    subject_with_lowest_plans = subjects_with_plans.order_by('num_plans').first()

    # Subject with highest and lowest number of teachers
    subject_with_highest_teachers = subjects_with_teachers.order_by('-num_teachers').first()
    subject_with_lowest_teachers = subjects_with_teachers.order_by('num_teachers').first()

    return render(request, 'teachers/dashboard.html', {
        'teacher': teacher,
        'subjects': subjects,
        'approved_lesson_plans': approved_lesson_plans,
        'pending_lesson_plans': pending_lesson_plans,
        'total_lesson_plans': total_lesson_plans,
        'total_pending_plans': total_pending_plans,
        'total_approved_plans': total_approved_plans,
        'subject_names': [subject.title for subject in subjects_with_plans],
        'num_plans': [subject.num_plans for subject in subjects_with_plans],
        'subject_with_highest_plans': subject_with_highest_plans,
        'subject_with_lowest_plans': subject_with_lowest_plans,
        'subject_names_teachers': subject_names_teachers,
        'num_teachers': num_teachers,
        'subject_with_highest_teachers': subject_with_highest_teachers,
        'subject_with_lowest_teachers': subject_with_lowest_teachers,
    })


@login_required
def create_lesson_plan(request):
    if request.method == 'POST':
        form = LessonPlanForm(request.POST)
        if form.is_valid():
            lesson_plan = form.save(commit=False)
            lesson_plan.teacher = Teacher.objects.get(user=request.user)
            lesson_plan.save()
            return redirect('teachers:dashboard')
    else:
        form = LessonPlanForm()
    return render(request, 'teachers/create_lesson_plan.html', {'form': form})

@login_required
def update_lesson_plan(request, lesson_plan_id):
    lesson_plan = get_object_or_404(LessonPlan, id=lesson_plan_id, teacher__user=request.user)
    if request.method == 'POST':
        form = LessonPlanForm(request.POST, instance=lesson_plan)
        if form.is_valid():
            form.save()
            return redirect('teachers:dashboard')
    else:
        form = LessonPlanForm(instance=lesson_plan)
    return render(request, 'teachers/update_lesson_plan.html', {'form': form, 'lesson_plan': lesson_plan})

@login_required
def delete_lesson_plan(request, lesson_plan_id):
    lesson_plan = get_object_or_404(LessonPlan, id=lesson_plan_id, teacher__user=request.user)
    if request.method == 'POST':
        lesson_plan.delete()
        return redirect('teachers:dashboard')
    return render(request, 'teachers/delete_lesson_plan.html', {'lesson_plan': lesson_plan})
