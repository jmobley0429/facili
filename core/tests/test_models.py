from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Discussion, Topic, FeedItem, Facilitator


class TestDiscussion(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(username="Jake")
        for i in range(3):
            title = f"The Title {i}"
            description = f"The description {i}"
            discussion = Discussion.objects.create(title=title, description=description)
            for i in range(3):
                title = f"The Title {i}"
                desc = f"The Desc {i}"
                topic = Topic.objects.create(
                    title=title, description=desc, discussion=discussion
                )
                facilitator = Facilitator.objects.create(
                    name="Ned Nameson", discussion=discussion, assoc_user=user
                )
                for i in range(3):
                    FeedItem.objects.create(
                        content="The feed content",
                        feedback="Some feedback",
                        upvotes=i,
                        downvotes=i,
                        topic=topic,
                        facilitator=facilitator,
                    )

    def test_str_returns_title(self):
        disc = Discussion.objects.last()
        self.assertEqual(str(disc), "The Title 0")

    def test_ordered_in_date_descending(self):
        discussions = Discussion.objects.all()
        ordered_correctly = []
        for i, d in enumerate(discussions):
            try:
                correct = d.date_added > discussions[i + 1].date_added
            except IndexError:
                correct = True
            ordered_correctly.append(correct)
        self.assertTrue(all(ordered_correctly))

    def test_get_absolute_url(self):
        pk = 1
        disc = Discussion.objects.get(pk=pk)
        url = disc.get_absolute_url()
        expected = f"/edit/{pk}"
        self.assertEqual(url, expected)

    def test_title_max_length(self):
        max_length = Discussion._meta.get_field("title").max_length
        self.assertEqual(100, max_length)

    def test_desc_max_length(self):
        max_length = Discussion._meta.get_field("description").max_length
        self.assertEqual(2000, max_length)

    def test_get_discussion_results(self):
        discussion = Discussion.objects.first()
        results = discussion.get_discussion_results()
        topics = discussion.topic_set.all()
        feeditems = [item for topic in topics for item in topic.feeditem_set.all()]

        self.assertTrue("topics" in results)
        self.assertTrue("feeditems" in results)
        self.assertEqual(feeditems, results["feeditems"])
        self.assertQuerysetEqual(topics, results["topics"])


class TestTopic(TestCase):
    @classmethod
    def setUp(cls):
        discussion = Discussion.objects.create(
            title="DiscTitle", description="DiscDesc"
        )
        for i in range(5):
            title = f"The Title {i}"
            description = f"The description {i}"
            topic = Topic.objects.create(
                title=title, description=description, discussion=discussion
            )

    def test_str_returns_title(self):
        topic = Topic.objects.last()
        self.assertEqual(str(topic), "The Title 0")

    def test_ordered_in_date_descending(self):
        topics = Topic.objects.all()

    def test_title_max_length(self):
        max_length = Topic._meta.get_field("title").max_length
        self.assertEqual(100, max_length)

    def test_desc_max_length(self):
        max_length = Topic._meta.get_field("description").max_length
        self.assertEqual(1000, max_length)


class TestFeedItem(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(username="Jake")
        discussion = Discussion.objects.create(
            title="DiscTitle", description="DiscDesc"
        )
        facilitator = Facilitator(
            name="Ned Nameson", discussion=discussion, assoc_user=user
        )

        topic = Topic.objects.create(
            title="Topic title", description="Topic description", discussion=discussion
        )
        facilitator.save()
        for i in range(5):
            content = f"The content {i}"
            feedback = f"The feedback {i}"
            FeedItem.objects.create(
                content=content, feedback=feedback, topic=topic, facilitator=facilitator
            )

    def test_str_returns_content(self):
        feeditem = FeedItem.objects.first()
        self.assertEqual(str(feeditem), "The content 4")

    def test_upvote(self):
        feeditem = FeedItem.objects.first()
        upvotes = feeditem.upvotes
        feeditem.upvote()
        self.assertEqual(feeditem.upvotes, upvotes + 1)

    def test_downvote(self):
        feeditem = FeedItem.objects.first()
        downvotes = feeditem.downvotes
        feeditem.downvote()
        self.assertEqual(feeditem.downvotes, downvotes + 1)

    def test_feeditem_ordered_by_time_added_descending(self):
        feeditems = FeedItem.objects.all()
        ordered_correctly = []
        for i, d in enumerate(feeditems):
            try:
                correct = d.time_added > feeditems[i + 1].time_added
            except IndexError:
                correct = True
            ordered_correctly.append(correct)
        self.assertTrue(all(ordered_correctly))
