from django import forms
from .models import Discussion, Topic, FeedItem, Facilitator


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "description"]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title", "description"]


class FacilitatorForm(forms.ModelForm):
    class Meta:
        model = Facilitator
        fields = ["name"]


class FeedItemForm(forms.ModelForm):
    class Meta:
        model = FeedItem
        fields = ["content"]
        labels = {
            "content": "Response",
        }
