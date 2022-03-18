from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from . import models, forms

CONFIG = {
    "discussion": {
        "model": models.Discussion,
        "form": forms.DiscussionForm,
        "redirect_url_name": "create",
        "template_name": "create.html",
        "fk_model": None,
    },
    "topic": {
        "model": models.Topic,
        "form": forms.TopicForm,
        "redirect_url_name": "edit",
        "template_name": "edit.html",
        "fk_model": models.Discussion,
    },
}


def get_fk_set(model, pk):
    fk_model = CONFIG[model]["fk_model"]
    model_instance = fk_model.objects.get(pk=pk)
    query_set = eval(f"model_instance.{model}_set.all()")
    return query_set


def get_standard_context(context, model=None):
    conf = CONFIG[model]
    model_instance = conf["model"]
    form_instance = conf["form"]
    fk_model = conf["fk_model"]
    if fk_model:
        pk = context["pk"]
        all_instances = get_fk_set(model, pk=pk)
    else:
        all_instances = model_instance.objects.all()

    context[f"all_{model}s"] = all_instances
    context["edit_form"] = form_instance()
    context["add_form"] = form_instance()
    return context


def process_forms(
    request,
    model=None,
    context=None,
):
    # unpack all config objects
    conf = CONFIG[model]
    form = conf["form"]
    url_name = conf["redirect_url_name"]
    model_class = conf["model"]
    template = conf["template_name"]

    # check for presence of edit form
    if f"edit-{model}" in request.POST:
        form_instance = form(request.POST)
        if not form_instance.is_valid():
            context["edit_form"] = form_instance
            return render(request, template, context)
        else:
            data = form_instance.cleaned_data
            pk = request.POST[f"edit-{model}"]
            model_instance = model_class.objects.get(pk=pk)
            model_instance.title = data["title"]
            model_instance.description = data["description"]
            model_instance.save()
            if model == "discussion":
                url = reverse(url_name)
            else:
                url = reverse(url_name, args=[pk])
            return HttpResponseRedirect(url)

    # else POST is for add form
    elif f"add-{model}" in data:
        form_instance = form(request.POST)
        if not form_instance.is_valid():
            context["add_form"] = form_instance
            return render(request, template, context)
        else:
            data = form_instance.cleaned_data
            model_instance = model_class.objects.create(data)
            model_instance.save()
            return HttpResponseRedirect(url)


class CreateView(View):
    template_name = "create.html"
    context = {"custom_h1": "Create Discussions"}

    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs["pk"]
        except KeyError:
            pk = models.Discussion.objects.all()[0].id
        self.context["pk"] = pk
        context = get_standard_context(self.context, "discussion")
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        return process_forms(request, model="discussion", context=self.context)


class EditView(View):
    template_name = "edit.html"
    context = {"custom_h1": "Add Topics"}

    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        if pk == None:
            pk = Discussion.objects.all()[0].id
        self.context["pk"] = pk
        context = get_standard_context(self.context, "topic")
        context["discussion"] = models.Discussion.objects.get(pk=pk)
        return render(request, self.template_name, context=context)

    def post(self, request, pk, *args, **kwargs):

        process_forms(request, model="topic", context=self.context)


class DiscussView(View):
    template_name = "discuss.html"
    context = {"custom_h1": "Discuss"}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)


class ReviewView(View):
    template_name = "review.html"
    context = {"custom_h1": "Review"}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)
