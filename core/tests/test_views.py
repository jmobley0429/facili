import sys

from django.test import TestCase
from django.urls import reverse
from core.models import Discussion, Topic, FeedItem, Facilitator
from core.views import get_standard_context, get_fk_set
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

    def test_get_standard_context_with_discussion(self):
        pk = self.discussion_id
        context = {"pk": pk}
        model = "discussion"
        new_context = get_standard_context(context, model)
        self.assertTrue("all_discussions" in new_context)
        self.assertTrue("edit_form" in new_context)
        self.assertTrue("add_form" in new_context)
        all_discs = Discussion.objects.all()
        self.assertQuerysetEqual(new_context["all_discussions"], all_discs)
        self.assertIsInstance(new_context["add_form"], DiscussionForm)
        self.assertIsInstance(new_context["edit_form"], DiscussionForm)

    def test_view_exists_at_correct_url(self):
        url = "/create/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_can_be_called_by_name(self):
        url = reverse("create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse("create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("create.html")

    # @unittest.skip("already failed")
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
        self.assertEqual(response.status_code, 200)
        new_num_discussions = len(Discussion.objects.all())
        self.assertTrue(new_num_discussions > num_discussions)

    # @unittest.skip("already failed")
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

        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_title, edited_discussion.title)
        self.assertEqual(new_description, edited_discussion.description)
        self.assertRedirects(
            response,
            reverse("create"),
        )


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

    def test_get_fk_set(self):
        pk = self.discussion_id
        queryset = get_fk_set("topic", pk)
        expected_queryset = Discussion.objects.first().topic_set.all()
        self.assertQuerysetEqual(queryset, expected_queryset)

    def test_get_standard_context_with_topic(self):
        pk = self.discussion_id
        context = {"pk": pk}
        model = "topic"
        new_context = get_standard_context(context, model)
        self.assertTrue("all_topics" in new_context)
        self.assertTrue("edit_form" in new_context)
        self.assertTrue("add_form" in new_context)
        all_discs = Topic.objects.all()
        self.assertQuerysetEqual(new_context["all_topics"], all_discs)
        self.assertIsInstance(new_context["add_form"], TopicForm)
        self.assertIsInstance(new_context["edit_form"], TopicForm)

    def test_view_exists_at_correct_url(self):
        pk = self.discussion_id
        url = f"/edit/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("edit.html")

    # @unittest.skip("already failed")
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
        self.assertEqual(response.status_code, 200)
        new_num_topics = len(Topic.objects.all())
        self.assertTrue(new_num_topics > num_topics)

    # @unittest.skip("already failed")
    def test_edit_topic(self):
        topic = Topic.objects.first()
        title = topic.title
        desc = topic.description
        pk = topic.id
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[pk])
        data = {
            "edit-topic": str(pk),
            "title": "A new title",
            "description": "A new desc",
        }
        response = self.client.post(url, data=data)
        edited_topic = Topic.objects.get(pk=pk)
        new_title = edited_topic.title
        new_description = edited_topic.description
        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_title, edited_topic.title)
        self.assertEqual(new_description, edited_topic.description)
        self.assertRedirects(response, reverse("edit-discussion", args=[pk]))
