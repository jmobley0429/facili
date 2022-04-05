from django.urls import include, path
from django.contrib.auth import urls as auth_urls
from . import views


urlpatterns = [
    path("create/", views.create, name="create"),
    path("edit/", views.edit, name="edit"),
    path("edit/<int:pk>", views.edit, name="edit-discussion"),
    path("share/<int:pk>", views.share, name="share-discussion"),
    path("discuss/", views.discuss, name="discuss"),
    path("discuss/<int:pk>", views.discuss, name="discuss-discussion"),
    path("results/", views.results, name="results"),
    path("results/<int:pk>", views.results, name="results-discussion"),
]

urlpatterns += auth_urls.urlpatterns[2:]
