import os
from . import conf


def make_url(href: str = ""):
    return os.path.join(conf.BASE_URL, href)
