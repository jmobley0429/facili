from django import forms
from .models import *


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "description"]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title", "description"]
