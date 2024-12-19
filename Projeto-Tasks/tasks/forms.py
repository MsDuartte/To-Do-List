from django import forms
from tasks.models import Task

class TaskModelForm(forms.ModelForm): 
    class Meta:
        model = Task
        exclude = ["datecompleted", "user", "status"]

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["datecompleted", "user"]
