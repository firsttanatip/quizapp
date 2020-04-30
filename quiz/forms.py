from django.forms import ModelForm
from .models import *


class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'
        

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'