from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from . import models, forms


def create(request):
    template_name = "create.html"
    context = {}
    context["custom_h1"] = "Create Discussion"
    context["edit_form"] = forms.DiscussionForm()
    context["add_form"] = forms.DiscussionForm()

    if request.method == "GET":
        all_discussions = models.Discussion.objects.all()
        context["all_discussions"] = all_discussions
        return render(request, template_name, context)

    elif request.method == "POST":
        if "add-discussion" in request.POST:
            form = forms.DiscussionForm(request.POST)
            if not form.is_valid():
                context["form"] = form
                return render(reverse("create"), template_name, context=context)
            else:
                form.save()
                return HttpResponseRedirect(reverse("create"))

        else:
            pk = request.POST["edit-discussion"]
            discussion = models.Discussion.objects.get(pk=pk)
            form = forms.DiscussionForm(request.POST, instance=discussion)
            if not form.is_valid():
                context["form"] = form
                return HttpResponseRedirect(reverse("create"))
            else:
                form.save()
                HttpResponseRedirect(reverse("create"))


def edit(request, pk=None):
    if pk == None:
        pk = models.Discussion.objects.first().id
    template_name = "edit.html"
    context = {}
    context["custom_h1"] = "Create Topic"
    context["edit_form"] = forms.TopicForm()
    context["add_form"] = forms.TopicForm()

    if request.method == "GET":
        all_topics = models.Topic.objects.all()
        context["all_topics"] = all_topics
        return render(request, template_name, context)

    elif request.method == "POST":
        if "add-topic" in request.POST:
            pk = request.POST["add-topic"]
            discussion = models.Discussion.objects.get(pk=pk)
            form = forms.TopicForm(request.POST)
            if not form.is_valid():
                context["form"] = form

                return HttpResponseRedirect(reverse("edit", args=[pk]))
            else:
                title = form.cleaned_data["title"]
                description = form.cleaned_data["description"]
                topic = models.Topic.objects.create(
                    title=title,
                    description=description,
                    discussion=discussion,
                )

                return HttpResponseRedirect(reverse("edit-discussion", args=[pk]))

        else:
            pk = request.POST["edit-topic"]
            parent_pk = request.POST["parent-discussion"]
            topic = models.Topic.objects.get(pk=pk)
            form = forms.TopicForm(request.POST, instance=topic)
            if not form.is_valid():
                context["form"] = form
                return render(request, template_name, context)

            else:
                form.save()
                return HttpResponseRedirect(
                    reverse("edit-discussion", args=[parent_pk])
                )


def discuss(request):
    return render(request, "discuss.html", {"custom_h1": "Discuss "})


def review(request):
    return render(request, "review.html", {"custom_h1": "Review "})
