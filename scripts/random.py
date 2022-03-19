from core.models import *
from collections import deque


def get_desc(dl):
    dl.rotate(10)
    return " ".join(list(dl)).capitalize()


discussions = Discussion.objects.all()

for d in discussions:
    d.delete()
lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum, enim. Iusto repellat, voluptatum suscipit. Quisquam distinctio adipisci natus velit fugiat vel blanditiis placeat corporis porro, voluptatibus pariatur at facilis numquam expedita cupiditate quae, molestias asperiores deleniti laudantium harum fuga officia voluptas qui illum incidunt! Beatae temporibus, veniam voluptas culpa? Perspiciatis."
titles = []
title = ""
for i, l in enumerate(lorem.split()):
    if i % 3 == 0:
        title = title.strip() + "?"
        titles.append(title)
        title = ""
    else:
        title += l + " "
titles = [title.capitalize() for title in titles[1:]]
dl = deque(lorem.split())

i = 0
for title in titles:
    d_desc = get_desc(dl)
    disc = Discussion.objects.create(title=title, description=d_desc)
    for t in titles:
        t_desc = get_desc(dl)
        topic = Topic.objects.create(title=title, description=t_desc, discussion=disc)
        topic.title = title
        topic.description = desc
        topic.save()
    disc.save()
