from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class Discussion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_added"]
        permissions = [
            ("can_edit", "Can edit Discussions"),
            ("can_add", "Can add Discussions"),
            ("can_delete", "Can delete Discussions"),
        ]

    def get_absolute_url(self):
        return reverse("edit-discussion", args=[str(self.pk)])

    def get_discussion_results(self):
        topics = self.topic_set.all()
        feeditems = [item for topic in topics for item in topic.feeditem_set.all()]

        return {
            "topics": topics,
            "feeditems": feeditems,
        }


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=True, null=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_added"]
        permissions = [
            ("can_edit", "Can edit Topics"),
            ("can_add", "Can add Topics"),
            ("can_delete", "Can delete Topics"),
        ]


class Facilitator(models.Model):
    name = models.CharField(max_length=50)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class FeedItem(models.Model):
    content = models.CharField(max_length=150)
    feedback = models.CharField(max_length=150)
    time_added = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0, blank=True)
    downvotes = models.PositiveIntegerField(default=0, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    facilitator = models.ForeignKey(Facilitator, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-time_added"]

    def __str__(self):
        return self.content

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1
