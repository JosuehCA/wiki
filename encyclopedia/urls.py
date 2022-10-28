from django.urls import path

from . import views

urlpatterns = [
    path("", views.error, name="error"),
    path("wiki/", views.index, name="index"),
    path("wiki/<str:input>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.NewEntry, name="new"),
    path("save/", views.SaveEntry, name="save"),
    path("edit/", views.edit, name="edit"),
    path("random/", views.random, name="random")
]
