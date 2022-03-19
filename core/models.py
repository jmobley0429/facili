from django.db import models
from django.urls import reverse


class Discussion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_added"]

    def get_absolute_url(self):
        return reverse("edit-discussion", args=[str(self.pk)])


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


class FeedItem(models.Model):
    content = models.CharField(max_length=150)
    feedback = models.CharField(max_length=150)
    time_added = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0, blank=True)
    downvotes = models.PositiveIntegerField(default=0, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1


class Facilitator(models.Model):
    name = models.CharField(max_length=50)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
