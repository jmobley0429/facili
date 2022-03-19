from django.test import TestCase
from django.urls import reverse
from core.models import Discussion, Topic, FeedItem, Facilitator
from core.forms import DiscussionForm, TopicForm
import unittest


class TestCreateView(TestCase):
    @property
    def discussion_id(self):
        return Discussion.objects.first().id

    @classmethod
    def setUp(cls):
        for i in range(10):
            title = f"The Title {i}"
            desc = f"The Desc {i}"
            Discussion.objects.create(title=title, description=desc)

    def test_view_exists_at_correct_url(self):
        url = "/create/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #
    def test_view_can_be_called_by_name(self):
        url = reverse("create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #
    def test_view_uses_correct_template(self):
        url = reverse("create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("create.html")

    #
    def test_add_new_discussion(self):
        num_discussions = len(Discussion.objects.all())
        url = reverse("create")
        pk = self.discussion_id
        data = {
            "add-discussion": str(pk),
            "title": "A new title",
            "description": "A new desc",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        new_num_discussions = len(Discussion.objects.all())
        self.assertTrue(new_num_discussions > num_discussions)

    def test_edit_discussion(self):
        discussion = Discussion.objects.first()
        title = discussion.title
        desc = discussion.description
        pk = discussion.id
        url = reverse("create")
        data = {
            "edit-discussion": str(pk),
            "title": "A new title",
            "desc": "A new desc",
        }
        response = self.client.post(url, data=data)
        edited_discussion = Discussion.objects.get(pk=pk)
        new_title = edited_discussion.title
        new_description = edited_discussion.description

        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_title, edited_discussion.title)
        self.assertEqual(new_description, edited_discussion.description)
        self.assertRedirects(
            response,
            reverse("create"),
        )


#
#
class TestEditView(TestCase):
    @classmethod
    def setUp(cls):

        discussion = Discussion.objects.create(title="A title", description="A desc")
        for i in range(10):
            title = f"The Title {i}"
            desc = f"The Desc {i}"
            topic = Topic.objects.create(
                title=title, description=desc, discussion=discussion
            )

    @property
    def discussion_id(self):
        return Discussion.objects.first().id

    def test_default_view_exists_at_correct_url(self):
        pk = self.discussion_id
        url = f"/edit/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_view_exists_at_correct_url(self):
        pk = self.discussion_id
        url = f"/edit/{pk}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_default_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("edit")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[str(pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #
    def test_view_uses_correct_template(self):
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("edit.html")

    #
    def test_add_new_topic(self):
        num_topics = len(Topic.objects.all())
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[pk])
        data = {
            "add-topic": str(pk),
            "title": "A new title",
            "description": "A new desc",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        new_num_topics = len(Topic.objects.all())
        self.assertTrue(new_num_topics > num_topics)

    #
    def test_edit_topic(self):
        topic = Topic.objects.first()
        title = topic.title
        desc = topic.description
        pk = topic.id
        parent_pk = self.discussion_id
        url = reverse("edit-discussion", args=[parent_pk])
        data = {
            "parent-discussion": parent_pk,
            "edit-topic": str(pk),
            "title": "A new title",
            "description": "A new desc",
        }
        response = self.client.post(url, data=data)
        edited_topic = Topic.objects.get(pk=pk)
        new_title = edited_topic.title
        new_description = edited_topic.description
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_title, edited_topic.title)
        self.assertEqual(new_description, edited_topic.description)
        self.assertRedirects(response, reverse("edit-discussion", args=[parent_pk]))
