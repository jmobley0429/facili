from django import forms
from .models import *


class DiscussionForm(forms.ModelForm):
    model = Discussion

    class Meta:
        fields = ["title", "description"]


class TopicForm(forms.ModelForm):
    model = Topic

    class Meta:
        fields = ["title", "description"]
