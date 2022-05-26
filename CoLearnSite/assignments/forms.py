from django.forms import ModelForm, DateInput, TimeInput, Form, DateTimeInput
from django import forms
from django.shortcuts import get_object_or_404
from assignments.models import SubmitAssignment, Assignment
from django.utils import timezone
from courses.models import Course
from users.models import User

class GradeAssignmentForm(ModelForm):
    
    class Meta:
        model = SubmitAssignment
        fields = ['grade']

class CreateAssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ('assignment_name', 'assignment_description',
                  'due_date', 'course') 
        labels = {
            'assignment_name': 'Name of the challenge',
            'assignment_description': 'Challenge description',
            'due_date': 'Due Date (yyyy-mm-dd HH:MM)' 
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
       

class SubmitAssignmentForm(ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = ('topic', 'description', 'assignment_file', 'assignment_ques', 'author')

        labels = {
            'description': 'Please state your work clear and short',
            'assignment_file': 'Your work',
            'assignment_ques': 'Please choose the related challenge'
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        assignment = kwargs.pop('assignment_id')
        super().__init__(*args, **kwargs)
        self.fields['assignment_ques'].queryset = self.fields['assignment_ques'].queryset.filter(pk=assignment)
        self.fields['author'].queryset = self.fields['author'].queryset.filter(username=user.username)