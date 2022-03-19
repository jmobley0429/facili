from django.test import TestCase
from core.models import Discussion, Topic, FeedItem, Facilitator


class TestDiscussion(TestCase):
    @classmethod
    def setUp(cls):
        for i in range(5):
            title = f"The Title {i}"
            description = f"The description {i}"
            discussion = Discussion.objects.create(title=title, description=description)

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
        expected = f"/edit/{pk}/"
        self.assertEqual(url, expected)

    def test_title_max_length(self):
        max_length = Discussion._meta.get_field("title").max_length
        self.assertEqual(100, max_length)

    def test_desc_max_length(self):
        max_length = Discussion._meta.get_field("description").max_length
        self.assertEqual(2000, max_length)


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
        ordered_correctly = []
        for i, t in enumerate(topics):
            try:
                correct = t.date_added > topics[i + 1].date_added
            except IndexError:
                correct = True
            ordered_correctly.append(correct)
        self.assertTrue(all(ordered_correctly))

    def test_title_max_length(self):
        max_length = Topic._meta.get_field("title").max_length
        self.assertEqual(100, max_length)

    def test_desc_max_length(self):
        max_length = Topic._meta.get_field("description").max_length
        self.assertEqual(1000, max_length)


class TestFeedItem(TestCase):
    @classmethod
    def setUp(cls):
        discussion = Discussion.objects.create(
            title="DiscTitle", description="DiscDesc"
        )

        topic = Topic.objects.create(
            title="Topic title", description="Topic description", discussion=discussion
        )
        for i in range(5):
            content = f"The content {i}"
            feedback = f"The feedback {i}"
            feeditem = FeedItem.objects.create(
                content=content, feedback=feedback, topic=topic
            )

    def test_str_returns_content(self):
        feeditem = FeedItem.objects.first()
        self.assertEqual(str(feeditem), "The content 0")

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
