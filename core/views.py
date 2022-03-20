from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Discussion, Topic, FeedItem, Facilitator
from .forms import DiscussionForm, TopicForm, FacilitatorForm


def create(request):
    template_name = "create.html"
    context = {}
    context["custom_h1"] = "Create Discussion"
    context["add_form"] = DiscussionForm()

    if request.method == "GET":
        all_discussions = Discussion.objects.all()
        edit_forms = []
        ids = []
        for disc in all_discussions:
            form = DiscussionForm(instance=disc)
            edit_forms.append(form)
            ids.append(disc.id)

        context["all_discussions"] = all_discussions
        context["edit_forms"] = edit_forms
        context["ids"] = ids
        return render(request, template_name, context)

    elif request.method == "POST":
        if "add-discussion" in request.POST:
            form = DiscussionForm(request.POST)
            if not form.is_valid():
                context["form"] = form
                return render(reverse("create"), template_name, context=context)
            else:
                form.save()
                return HttpResponseRedirect(reverse("create"))

        else:
            pk = request.POST["edit-discussion"]
            form = DiscussionForm(request.POST)
            if not form.is_valid():
                context["form"] = form
                return HttpResponseRedirect(reverse("create"))
            else:
                form.save()
                return HttpResponseRedirect(reverse("create"))


def edit(request, pk=None):
    if pk == None:
        pk = Discussion.objects.first().id
    template_name = "edit.html"
    context = {}
    context["custom_h1"] = "Add Topic"
    context["edit_form"] = TopicForm()
    context["add_form"] = TopicForm()

    if request.method == "GET":
        all_topics = Topic.objects.all()
        context["all_topics"] = all_topics
        return render(request, template_name, context)

    elif request.method == "POST":
        if "add-topic" in request.POST:
            pk = request.POST["add-topic"]
            discussion = Discussion.objects.get(pk=pk)
            form = TopicForm(request.POST)
            if not form.is_valid():
                context["form"] = form
                return HttpResponseRedirect(reverse("edit"))
            else:
                title = form.cleaned_data["title"]
                description = form.cleaned_data["description"]
                topic = Topic.objects.create(
                    title=title,
                    description=description,
                    discussion=discussion,
                )

                return HttpResponseRedirect(reverse("edit-discussion", args=[pk]))

        else:
            pk = request.POST["edit-topic"]
            parent_pk = request.POST["parent-discussion"]
            topic = Topic.objects.get(pk=pk)
            form = TopicForm(request.POST, instance=topic)
            if not form.is_valid():
                context["form"] = form
                return render(request, template_name, context)

            else:
                form.save()
                return HttpResponseRedirect(
                    reverse("edit-discussion", args=[parent_pk])
                )


def share(request, pk):
    template_name = "share.html"
    context = {"custom_h1": "Share Discussion"}
    if request.method == "GET":
        discussion = Discussion.objects.get(pk=pk)
        fac = Facilitator(discussion=discussion)
        form = FacilitatorForm(instance=fac)
        context["form"] = form
        return render(request, template_name, context)

    elif request.method == "POST":
        form = FacilitatorForm(request.POST)
        if not form.is_valid():
            context["form"] = form
            return render(request, template_name, context)
        else:
            form.save()
            return HttpResponseRedirect(reverse("discuss-discussion", args=[pk]))


def discuss(request, pk=None):
    template_name = "discuss.html"
    if pk == None:
        pk = Discussion.objects.first().id
    context = {
        "custom_h1": "Start Discussion",
        "pk": pk,
    }
    return render(request, template_name, context)


def review(request):
    return render(request, "review.html", {"custom_h1": "Review "})
