from django.contrib import admin
from .models import Title, Teacher, Subject, PlanDetails, LessonPlan

class TitleAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Title, TitleAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'name', 'email', 'address']
    list_filter = ['title']

admin.site.register(Teacher, TeacherAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Subject, SubjectAdmin)

class PlanDetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(PlanDetails, PlanDetailsAdmin)

class LessonPlanAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'subject', 'date', 'plan_details', 'submission_status']
    list_filter = ['teacher', 'subject', 'submission_status']
    search_fields = ['teacher__user__username', 'subject__title', 'submission_status']

admin.site.register(LessonPlan, LessonPlanAdmin)

# Customize admin site details for Cloud-Based Lesson Note Submission and Evaluation Information Management System
admin.site.site_header = "Lesson Note System Admin"
admin.site.site_title = "Lesson Note Admin"
admin.site.index_title = "Welcome to the Lesson Note System Admin Panel"
admin.site.site_url = "/home/"