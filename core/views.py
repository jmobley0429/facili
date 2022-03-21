from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Discussion, Topic, FeedItem, Facilitator
from .forms import DiscussionForm, TopicForm, FacilitatorForm
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    template_name = "create.html"
    context = {}
    context["custom_h1"] = "Create Discussion"
    context["add_form"] = DiscussionForm()

    if request.method == "GET":
        all_discussions = Discussion.objects.all()
        edit_forms = []
        for disc in all_discussions:
            form = DiscussionForm()
            edit_forms.append(form)
        context["discussion_zip"] = list(zip(all_discussions, edit_forms))
        return render(request, template_name, context)

    elif request.method == "POST":
        if "add-discussion" in request.POST:
            form = DiscussionForm(request.POST)
            if not form.is_valid():
                context["form"] = form
                return render(request, template_name, context=context)
            else:
                form.save()
                return HttpResponseRedirect(reverse("create"))

        else:
            pk = request.POST["edit-discussion"]
            print("initial POST: ", request.POST)
            discussion = Discussion.objects.get(pk=pk)
            print("initial discussion: ", discussion)
            form = DiscussionForm(request.POST)
            print("initial form: ", form)
            if not form.is_valid():
                context["form"] = form
                return render(request, template_name, context)
            else:
                data = form.cleaned_data
                print("Cleaned data: ", data)
                discussion.title = data["title"]
                discussion.description = data["description"]
                discussion.save(update_fields=["title", "description"])
                print("Saved Discussion: ", discussion)
                return HttpResponseRedirect(reverse("create"))


@login_required
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
            topic = Topic(discussion=discussion)
            form = TopicForm(request.POST, instance=topic)
            if not form.is_valid():
                context["form"] = form
                return render(request, template_name, context)
            else:
                form.save()
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
        form = FacilitatorForm()
        context["form"] = form
        return render(request, template_name, context)
    elif request.method == "POST":
        discussion = Discussion.objects.get(pk=pk)
        facilitator = Facilitator(discussion=discussion)
        form = FacilitatorForm(request.POST, instance=facilitator)
        if not form.is_valid():
            context["form"] = form
            return render(request, template_name, context)
        else:
            form.save()
            return HttpResponseRedirect(reverse("discuss-discussion", args=[pk]))


def discuss(request, pk=None):
    template_name = "discuss.html"
    context = {"custom_h1": "Start Discussion"}
    if pk == None:
        context["none-selected"] = True
        return render(request, template_name, context)
    if request.method == "GET":
        discussion = Discussion.objects.get(pk=pk)
        facilitators = discussion.facilitator_set.all()
        topics = discussion.topic_set.all()
        context["facilitators"] = facilitators
        context["discussion"] = discussion
        context["topics"] = topics
        return render(request, template_name, context)


def results(request, pk=None):
    template_name = "results.html"
    context = {"custom_h1": "Review Discussion"}
    if pk == None:
        context["none-selected"] = True
        return render(request, template_name, context)
    if request.method == "GET":
        discussion = Discussion.objects.get(pk=pk)
        context["results"] = discussion.get_discussion_results()
        context["discussion"] = discussion
        return render(request, template_name, context)
