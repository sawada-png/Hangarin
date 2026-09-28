from django.contrib import admin
from django.urls import include, path

from taskmanager.views import (
    HomePageView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    NoteListView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
    SubTaskListView,
    SubTaskCreateView,
    SubTaskUpdateView,
    SubTaskDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include("allauth.urls")),

    path(
        "",
        HomePageView.as_view(),
        name="home"
    ),

    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),

    path(
        "tasks/add/",
        TaskCreateView.as_view(),
        name="task-add"
    ),

    path(
        "tasks/<int:pk>/edit/",
        TaskUpdateView.as_view(),
        name="task-edit"
    ),

    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),

    path(
        "notes/",
        NoteListView.as_view(),
        name="note-list"
    ),

    path(
        "notes/add/",
        NoteCreateView.as_view(),
        name="note-add"
    ),

    path(
        "notes/<int:pk>/edit/",
        NoteUpdateView.as_view(),
        name="note-edit"
    ),

    path(
        "notes/<int:pk>/delete/",
        NoteDeleteView.as_view(),
        name="note-delete"
    ),

    path(
        "subtasks/",
        SubTaskListView.as_view(),
        name="subtask-list"
    ),

    path(
        "subtasks/add/",
        SubTaskCreateView.as_view(),
        name="subtask-add"
    ),

    path(
        "subtasks/<int:pk>/edit/",
        SubTaskUpdateView.as_view(),
        name="subtask-edit"
    ),

    path(
        "subtasks/<int:pk>/delete/",
        SubTaskDeleteView.as_view(),
        name="subtask-delete"
    ),
]