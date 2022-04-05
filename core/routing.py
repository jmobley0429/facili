from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/topic/(?P<topic>\w+)/$", consumers.TopicChatConsumer.as_asgi()),
]
