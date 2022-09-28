from django import forms
from todolist.models import Task
from django.forms import ModelForm
class FormTask(ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'date', 'title', 'description')
        exclude = ['user', 'date']