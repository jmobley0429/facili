import unittest
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from core.models import Discussion, Topic, FeedItem, Facilitator
from core.forms import DiscussionForm, TopicForm


def create_database(n=3, create_user=False):
    """
    creates a test database. n = the number of levels deep required for testing:
    0 : just create one discussion
    1 : Discussion with topics
    2 : Discussion with topics and facilitator
    3 : Discussion, topics, facilitator and discussion feeditems
    """
    discussion = Discussion.objects.create(title="A title", description="A desc")
    if n == 0:
        return
    for i in range(10):
        title = f"The Title {i}"
        desc = f"The Desc {i}"
        topic = Topic.objects.create(
            title=title, description=desc, discussion=discussion
        )
        if n == 1:
            break
        fac = Facilitator(name="Ned Nameson", discussion=discussion)
    if n < 3:
        return
        for i in range(10):
            data = {
                "content": "The feed content",
                "feedback": "Some feedback",
                "upvotes": i,
                "downvotes": i,
                "topic": topic,
                "facilitator": facilitator,
            }
            feeditem = FeedItem(data)
            feeditem.save()
    if create_user:
        test_user = User.objects.create_user(
            username="TestUser", password="aQ)vz3a^d5454"
        )
        test_user.save()


class TestCreateView(TestCase):
    @property
    def discussion_id(self):
        return Discussion.objects.first().id

    @classmethod
    def setUp(cls):
        for i in range(10):
            create_database(n=0, create_user=True)

    def test_user_cannot_access_page_without_login(self):
        url = "/create/"
        response = self.client.get(url)
        self.assertRedirects(response, f"/accounts/login/?next={url}")

    def test_view_exists_at_correct_url(self):
        url = "/create/"
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_request_context(self):
        url = f"/create/"
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        context = response.context
        self.assertEqual(response.status_code, 200)
        self.assertTrue("custom_h1" in context)
        self.assertTrue("all_discussions" in context)
        self.assertTrue("edit_forms" in context)
        self.assertTrue("ids" in context)
        self.assertEqual(context["custom_h1"], "Create Discussion")
        all_discussions = Discussion.objects.all()
        self.assertQuerysetEqual(context["all_discussions"], all_discussions)

    def test_view_can_be_called_by_name(self):
        url = reverse("create")
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #
    def test_view_uses_correct_template(self):
        url = reverse("create")
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create.html")

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
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
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
            "description": "A new desc",
        }
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
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

    def test_invalid_add_form_rejects_and_returns(self):
        discussion = Discussion.objects.first()
        pk = discussion.id
        url = reverse("create")
        data = {
            "add-discussion": "",
            "title": "",
            "description": "",
        }
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)

    def test_invalid_edit_form_rejects_and_returns(self):
        discussion = Discussion.objects.first()
        pk = discussion.id
        url = reverse("create")
        data = {
            "edit-discussion": str(pk),
            "title": "",
            "description": "",
        }
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)


#
#
class TestEditView(TestCase):
    @classmethod
    def setUp(cls):
        create_database(n=1, create_user=True)

    @property
    def discussion_id(self):
        return Discussion.objects.first().id

    def test_user_cannot_access_page_without_login(self):
        url = "/edit/"
        response = self.client.get(url)
        self.assertRedirects(response, f"/accounts/login/?next={url}")

    def test_default_view_exists_at_correct_url(self):
        url = f"/edit/"
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_request_context(self):
        pk = self.discussion_id
        url = f"/edit/{pk}"
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        context = response.context
        self.assertEqual(response.status_code, 200)
        self.assertTrue("custom_h1" in context)
        self.assertTrue("all_topics" in context)
        self.assertEqual(context["custom_h1"], "Add Topic")
        all_topics = Discussion.objects.get(pk=pk).topic_set.all()
        self.assertQuerysetEqual(context["all_topics"], all_topics)

    def test_post_request_context(self):
        pk = self.discussion_id
        url = f"/edit/{pk}"
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        context = response.context
        self.assertEqual(response.status_code, 200)
        self.assertTrue("custom_h1" in context)
        self.assertTrue("edit_form" in context)
        self.assertTrue("add_form" in context)
        self.assertEqual(context["custom_h1"], "Add Topic")

    def test_edit_view_exists_at_correct_url(self):
        pk = self.discussion_id
        url = f"/edit/{pk}"
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_default_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("edit")
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[str(pk)])
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #
    def test_view_uses_correct_template(self):
        pk = self.discussion_id
        url = reverse("edit-discussion", args=[pk])
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit.html")

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
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
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
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.post(url, data=data)
        edited_topic = Topic.objects.get(pk=pk)
        new_title = edited_topic.title
        new_description = edited_topic.description
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_title, edited_topic.title)
        self.assertEqual(new_description, edited_topic.description)
        self.assertRedirects(response, reverse("edit-discussion", args=[parent_pk]))

    def test_invalid_edit_topic_form_rejects_and_returns(self):
        discussion = Discussion.objects.first()
        topic_id = discussion.topic_set.first().id
        pk = discussion.id
        url = reverse("edit-discussion", args=[pk])
        data = {
            "edit-topic": str(topic_id),
            "parent-discussion": discussion.id,
            "title": "",
            "description": "",
        }
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)

    def test_invalid_add_topic_form_rejects_and_returns(self):
        discussion = Discussion.objects.first()
        pk = discussion.id
        url = reverse("edit-discussion", args=[pk])
        data = {
            "add-topic": pk,
            "title": "",
            "description": "",
        }
        self.client.force_login(User.objects.get_or_create(username="TestUser")[0])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)


class TestShareView(TestCase):
    @classmethod
    def setUp(cls):
        create_database(n=1)

    @property
    def discussion_id(self):
        return Discussion.objects.first().id

    def test_share_view_exists_at_correct_url(self):
        pk = self.discussion_id
        url = f"/share/{pk}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_share_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("share-discussion", args=[str(pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        pk = self.discussion_id
        url = reverse("share-discussion", args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "share.html")

    def test_can_add_facilitator(self):
        pk = self.discussion_id
        url = reverse("share-discussion", args=[pk])
        discussion = Discussion.objects.get(pk=pk)
        num_facilitators = len(discussion.facilitator_set.all())
        self.assertTrue(num_facilitators == 0)
        data = {
            "name": "Ned Nameson",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        new_disc = Discussion.objects.get(pk=pk)
        added_fac = new_disc.facilitator_set.first()
        name = added_fac.name
        self.assertEqual(name, "Ned Nameson")
        redirect_url = reverse("discuss-discussion", args=[pk])
        self.assertRedirects(response, redirect_url)

    def test_invalid_facilitator_form_rejects_and_returns(self):
        discussion = Discussion.objects.first()
        pk = discussion.id
        url = reverse("share-discussion", args=[pk])
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)


class TestDiscussView(TestCase):
    @classmethod
    def setUp(cls):
        create_database(n=2)

    @property
    def discussion_id(self):
        return Discussion.objects.first().id

    def test_discuss_view_exists_at_correct_url(self):
        pk = self.discussion_id
        url = f"/discuss/{pk}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_discuss_default_view_can_be_called_by_name(self):
        url = reverse("discuss")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_discuss_default_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("discuss-discussion", args=[str(pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse("discuss")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "discuss.html")

    def test_get_request_context(self):
        pk = self.discussion_id
        url = reverse("discuss-discussion", args=[pk])
        response = self.client.get(url)
        context = response.context
        self.assertTrue("custom_h1" in context)
        self.assertTrue("discussion" in context)
        self.assertTrue("facilitators" in context)
        self.assertTrue("topics" in context)


class TestResultsView(TestCase):
    @classmethod
    def setUp(cls):
        create_database(n=3)

    @property
    def discussion_id(self):
        return Discussion.objects.first().id

    def test_results_view_exists_at_correct_url(self):
        pk = self.discussion_id
        url = f"/results/{pk}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_results_default_view_can_be_called_by_name(self):
        url = reverse("results")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_results_default_view_can_be_called_by_name(self):
        pk = self.discussion_id
        url = reverse("results-discussion", args=[str(pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse("results")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "results.html")

    def test_get_request_context(self):
        pk = self.discussion_id
        url = reverse("results-discussion", args=[pk])
        response = self.client.get(url)
        context = response.context
        self.assertTrue("custom_h1" in context)
        self.assertTrue("discussion" in context)
        self.assertTrue("results" in context)
