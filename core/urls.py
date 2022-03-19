from django.urls import include, path
from . import views


urlpatterns = [
    path("create/", views.create, name="create"),
    path("edit/", views.edit, name="edit"),
    path("edit/<int:pk>", views.edit, name="edit-discussion"),
    path("discuss/", views.discuss, name="discuss"),
    path("review/", views.review, name="review"),
]
