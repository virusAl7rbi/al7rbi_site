from django.shortcuts import render, redirect
from .models import Apps, Comments
from .forms import CommentForm, VoteForm, SuggestionForm


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
        app_detail = None
        print(slug)
        print(e)

    if request.method == "POST":
        if "comment" in request.POST:
            form = CommentForm(request.POST)
        elif "suggestion" in request.POST:
            form = SuggestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.app = app_detail
            obj.save()
        return redirect("apps:app_details", slug)
    else:
        comment_form = CommentForm()
        suggestion_form = SuggestionForm()
        context = {
            "app": app_detail,
            "comment_form": comment_form,
            "suggestion_form": suggestion_form,
        }
        return render(request, "details.html", context)


def vote(request, slug=None):
    if request.method == "POST":
        VoteForm(request.POST).save()
        slug = request.POST["slug"]
        app_detail = Apps.objects.get(slug=slug)
        return redirect("apps:app_details", slug)
