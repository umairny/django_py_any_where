from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("project", views.ProjectListView.as_view()),
]
