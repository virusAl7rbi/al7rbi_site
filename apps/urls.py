from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.apps_list, name="apps_list"),
    path("<slug:slug>", views.app_details, name="app_details"),
    path("<slug:slug>/vote", views.vote, name="vote"),
    
    # class view
    #apps
    path("api/v2/apps", api.All_apps.as_view(), name="app_list_API_class"),
    path("api/v2/apps/<str:slug>", api.app_detail_api.as_view(), name="app_API_class"),
    path("api/v2/github", api.github_webhook, name="github_webhook"),
    #comments
    path("api/v2/comments", api.All_comments.as_view(), name="comments_API_class"),
    path("api/v2/comments/<str:app_id>", api.app_comments.as_view(), name="app_comments_API_class"),
    path('ajax_comment/<str:slug>', views.ajax_comment, name='ajax_comment'),# ajax-posting / name = that we will use in ajax url
    #Suggestion
    path("api/v2/suggestion", api.All_Suggestion.as_view(), name="app_Suggestion_class"),
    path("api/v2/suggestion/<str:app>", api.app_Suggestion.as_view(), name="add_Suggestion_class"),
    path('ajax_suggestion/<str:slug>', views.ajax_suggestion, name='ajax_suggestion'),# ajax-posting / name = that we will use in ajax url
    #vote
    path("api/v2/votes", api.All_votes.as_view(), name="app_votes_class"),
]