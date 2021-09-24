from django.urls import path
from . import views

urlpatterns = [
    path('', views.apps_list, name="apps_list"),
    path("<str:slug>", views.app_details, name="app_details"),
    path("<str:slug>/vote", views.vote, name="vote"),
]