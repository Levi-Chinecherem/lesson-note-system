# evaluations/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from teachers.models import LessonPlan
from .models import Evaluation, Evaluator
from .forms import EvaluationForm

# Define a custom test function
def is_evaluator(user):
    try:
        # Check if the user has an associated Evaluator instance
        return hasattr(user, 'evaluator') or Evaluator.objects.filter(user=user).exists()
    except Evaluator.DoesNotExist:
        return False

@login_required
@user_passes_test(is_evaluator, login_url='home:home')
def evaluate_lesson_plan(request, lesson_plan_id):
    lesson_plan = get_object_or_404(LessonPlan, pk=lesson_plan_id)
    evaluator = request.user.evaluator

    try:
        evaluation = Evaluation.objects.get(lesson_plan=lesson_plan, evaluator=evaluator)
    except Evaluation.DoesNotExist:
        evaluation = None

    if request.method == 'POST':
        form = EvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.lesson_plan = lesson_plan
            evaluation.evaluator = evaluator
            evaluation.save()

            # Update the lesson plan submission status based on the form selection
            submission_status = form.cleaned_data['submission_status']
            lesson_plan.submission_status = submission_status
            lesson_plan.save()

            messages.success(request, 'Evaluation submitted successfully.')
            return redirect('evaluations:evaluation_list')
    else:
        form = EvaluationForm(instance=evaluation)

    return render(request, 'evaluations/evaluate_lesson_plan.html', {'form': form, 'lesson_plan': lesson_plan, 'evaluation': evaluation})

@login_required
@user_passes_test(is_evaluator, login_url='home:home')
def evaluation_list(request):
    evaluations = Evaluation.objects.filter(evaluator=request.user.evaluator)
    return render(request, 'evaluations/evaluation_list.html', {'evaluations': evaluations})

@login_required
@user_passes_test(is_evaluator, login_url='home:home')
def evaluation_details(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, pk=evaluation_id, evaluator=request.user.evaluator)
    return render(request, 'evaluations/evaluation_details.html', {'evaluation': evaluation})

@login_required
@user_passes_test(is_evaluator, login_url='home:home')
def delete_evaluation(request, lesson_plan_id):
    lesson_plan = get_object_or_404(LessonPlan, pk=lesson_plan_id)
    evaluator = request.user.evaluator

    try:
        evaluation = Evaluation.objects.get(lesson_plan=lesson_plan, evaluator=evaluator)
        evaluation.delete()
        messages.success(request, 'Evaluation deleted successfully.')
    except Evaluation.DoesNotExist:
        messages.error(request, 'Evaluation does not exist.')

    return redirect('evaluations:evaluation_list')
