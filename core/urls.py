from django.urls import include, path
from . import views


urlpatterns = [
    path("create/", views.CreateView.as_view(), name="create"),
    path("edit/<int:pk>/", views.EditView.as_view(), name="edit"),
    path("discuss/<int:pk>/", views.DiscussView.as_view(), name="discuss"),
    path("review/<int:pk>/", views.ReviewView.as_view(), name="review"),
]
