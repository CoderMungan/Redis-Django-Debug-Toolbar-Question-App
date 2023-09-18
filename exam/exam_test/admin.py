from django.contrib import admin
from .models import Question,Answer
from django.contrib.auth.models import User

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','id')  

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_question_text', 'answer_text')
    list_filter =('user','question',)

