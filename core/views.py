from django.shortcuts import render
from django.views import View


class CreateView(View):
    template_name = "create.html"
    context = {"custom_h1": "Create"}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)


class EditView(View):
    template_name = "edit.html"
    context = {"custom_h1": "Edit"}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)


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
