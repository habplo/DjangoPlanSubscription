from django.forms import ModelForm
from .models import tasks


class TasksForm(ModelForm):
    class Meta:
        model = tasks
        fields = ['title']