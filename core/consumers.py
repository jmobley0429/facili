import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Topic, Facilitator, FeedItem
import pprint as p


class TopicChatConsumer(WebsocketConsumer):
    def connect(self):
        pk = self.scope["url_route"]["kwargs"]["topic"]
        self.facilitator = self.scope["user"].username
        self.topic = Topic.objects.get(pk=pk)
        self.topic_chat = f"topic_{self.topic.id}"
        async_to_sync(self.channel_layer.group_add)(self.topic_chat, self.channel_name)
        self.accept()

    def disconnect(self, close_mode):
        async_to_sync(self.channel_layer.group_discard)(
            self.topic_chat, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json["content"]
        fac = Facilitator.objects.get(name=self.facilitator)
        FeedItem.objects.create(content=content, facilitator=fac, topic=self.topic)
        async_to_sync(self.channel_layer.group_send)(
            self.topic_chat,
            {
                "type": "discussion_response",
                "content": content,
            },
        )

    def discussion_response(self, event):
        content = event["content"]
        self.send(
            text_data=json.dumps({"content": content, "facilitator": self.facilitator})
        )
