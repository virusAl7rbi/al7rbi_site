from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.apps_list, name="apps_list"),
    path("<str:slug>", views.app_details, name="app_details"),
    path("<str:slug>/vote", views.vote, name="vote"),
    
    # class view
    #apps
    path("api/v2/apps", api.All_apps.as_view(), name="app_list_API_class"),
    path("api/v2/apps/<str:slug>", api.app_detail_api.as_view(), name="app_API_class"),
    #comments
    path("api/v2/comments", api.All_comments.as_view(), name="comments_API_class"),
    path("api/v2/comments/<str:app_id>", api.app_comments.as_view(), name="app_comments_API_class"),
    #Suggestion
    path("api/v2/suggestion", api.All_Suggestion.as_view(), name="app_Suggestion_class"),
    path("api/v2/suggestion/<str:app>", api.app_Suggestion.as_view(), name="add_Suggestion_class"),
    #vote
    path("api/v2/votes", api.All_votes.as_view(), name="app_votes_class"),
]