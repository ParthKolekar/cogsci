from django.contrib import admin
from .models import Comprehension, Question, Submission


# Register your models here.

@admin.register(Comprehension)
class ComprehensionAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    pass
