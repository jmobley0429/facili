from django.db import models


class Discussion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=True, null=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)


class FeedItem(models.Model):
    content = models.CharField(max_length=150)
    feedback = models.CharField(max_length=150)
    upvotes = models.PositiveIntegerField(null=True, blank=True)
    downvotes = models.PositiveIntegerField(null=True, blank=True)
    discussion = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Facilitator(models.Model):
    name = models.CharField(max_length=50)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
