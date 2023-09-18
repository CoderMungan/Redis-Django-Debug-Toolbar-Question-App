from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


    
class Question(models.Model):
    question_text=models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
    
    def get_question_text(self):
        return self.question.question_text

    def get_username(self):
        return self.user.username
    
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'question'], name='unique_user_question_answer')
        ]
        unique_together = ('question', 'user')

