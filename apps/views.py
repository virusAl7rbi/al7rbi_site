from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotFound
from .forms import CommentForm, VoteForm, SuggestionForm
from django.core.paginator import Paginator
from .models import Apps


# configuration area
app_name = "apps"


def apps_list(request):
    all_apps = Apps.objects.all()
    if len(all_apps) <= 2:
        app_list = [list(all_apps)]
    else:
        app_list = [all_apps[i::2] for i in range(2)]
    return render(request, "index.html", {"apps_list": app_list})


def app_details(request, slug):
    try:
        app_detail = Apps.objects.get(slug=slug)
    except Apps.DoesNotExist as e:
        app_detail = False
    comment_form = CommentForm()
    suggestion_form = SuggestionForm()
    context = {
            "app": app_detail,
            "comment_form": comment_form,
            "suggestion_form": suggestion_form,
        }
    if app_detail:
        return render(request, "details.html", context)
    else:
        return HttpResponseNotFound("Wrong page")


def vote(request, slug=None):
    if request.method == "POST":
        VoteForm(request.POST).save()
        slug = request.POST["slug"]
        app_detail = Apps.objects.get(slug=slug)
        return redirect("apps:app_details", slug)


# ajax_posting function
def ajax_comment(request, slug):
    try:
        app_detail = Apps.objects.get(slug=slug)
    except Apps.DoesNotExist as e:
        app_detail = None
    if request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.app = app_detail
            obj.save()
            return JsonResponse({
                         'msg':'ok' # response message
            }) # return response as JSON
            
# ajax_posting function
def ajax_suggestion(request, slug):
    try:
        app_detail = Apps.objects.get(slug=slug)
    except Apps.DoesNotExist as e:
        app_detail = None
    if request.is_ajax():
        form = SuggestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.app = app_detail
            obj.save()
            return JsonResponse({
                         'msg':'ok' # response message
            }) # return response as JSON