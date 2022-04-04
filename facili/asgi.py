import os

import django
from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "facili.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
    }
)
