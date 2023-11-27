from django import forms
from django.contrib.auth import get_user_model

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "content",
            "deadline",
            "tags"
        )
