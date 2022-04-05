from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from .models import Discussion, Topic, FeedItem, Facilitator
from .forms import DiscussionForm, TopicForm, FacilitatorForm, FeedItemForm
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
            ("initial POST: ", request.POST)
            discussion = Discussion.objects.get(pk=pk)
            ("initial discussion: ", discussion)
            form = DiscussionForm(request.POST)
            ("initial form: ", form)
            if not form.is_valid():
                context["form"] = form
                return render(request, template_name, context)
            else:
                data = form.cleaned_data
                ("Cleaned data: ", data)
                discussion.title = data["title"]
                discussion.description = data["description"]
                discussion.save(update_fields=["title", "description"])
                ("Saved Discussion: ", discussion)
                return HttpResponseRedirect(reverse("create"))


@login_required
def edit(request, pk=None):
    if pk is None:
        pk = Discussion.objects.first().id
    template_name = "edit.html"
    context = {}
    context["custom_h1"] = "Add Topic"
    context["edit_form"] = TopicForm()
    context["add_form"] = TopicForm()

    if request.method == "GET":
        all_discussions = Discussion.objects.all()
        discussion = Discussion.objects.get(pk=pk)
        context["discussion"] = discussion
        all_topics = discussion.topic_set.all()
        context["all_topics"] = all_topics
        context["all_discussions"] = all_discussions
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
        if "select-discussion" in request.POST:
            pk = request.POST["select-discussion"]
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
    previous_users = Facilitator.objects.all()
    context["previous_users"] = previous_users
    if request.method == "GET":
        form = FacilitatorForm()
        context["form"] = form
        return render(request, template_name, context)
    elif request.method == "POST":
        prev = request.POST["previous-users"]
        new = request.POST["new-facilitator"]
        discussion = Discussion.objects.get(pk=pk)
        if not prev and not new:
            context["warning"] = "Please enter a name or select from previous users"
            return render(request, template_name, context)
        elif prev:
            user_id = request.POST["previous-users"]
            user = User.objects.get(pk=user_id)
        elif new:
            username = new
            user = User.objects.create(username=username)
        Facilitator.objects.create(
            name=user.username, assoc_user=user, discussion=discussion
        )
        return HttpResponseRedirect(reverse("discuss-discussion", args=[pk]))


def discuss(request, pk=None):
    template_name = "discuss.html"
    context = {"custom_h1": "Start Discussion"}
    context["all_discussions"] = Discussion.objects.all()
    if request.method == "GET":
        if pk is not None:
            discussion = Discussion.objects.get(pk=pk)
            all_topics = discussion.topic_set.all()
            context["discussion"] = discussion
            context["facilitators"] = discussion.facilitator_set.all()
            feed_forms = [FeedItemForm(instance=t) for t in all_topics]
            context["all_topics_zip"] = zip(all_topics, feed_forms)
            return render(request, template_name, context)
        else:
            return render(request, template_name, context)
    if request.method == "POST":
        if "select-discussion" in request.POST:
            pk = request.POST["select-discussion"]
            return HttpResponseRedirect(reverse("discuss-discussion", args=[str(pk)]))
        elif "response" in request.POST:
            topic_id = request.POST["submit-response"]
            topic = Topic.objects.get(pk=topic_id)
            form = FeedItemForm(request.POST, instance=Topic)
            if form.is_valid():
                form.save()
                HttpResponseRedirect(request.POST["next"])


def results(request, pk=None):
    template_name = "results.html"
    context = {"custom_h1": "Review Discussion"}
    if pk is None:
        context["none-selected"] = True
        return render(request, template_name, context)
    if request.method == "GET":
        discussion = Discussion.objects.get(pk=pk)
        context["results"] = discussion.get_discussion_results()
        context["discussion"] = discussion
        return render(request, template_name, context)
        context["discussion"] = discussion
        return render(request, template_name, context)
