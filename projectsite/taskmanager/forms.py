from django import forms

from .models import Task, Note, SubTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "deadline",
            "status",
            "category",
            "priority",
        ]

        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local"
                }
            ),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "task",
            "content",
        ]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Write your note here..."
                }
            ),
        }


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = [
            "task",
            "title",
            "status",
        ]