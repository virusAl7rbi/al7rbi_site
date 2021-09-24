from django.shortcuts import render, redirect
from .models import Apps
from .forms import CommentForm, VoteForm


app_name = 'apps'

def apps_list(request):
    all_apps = Apps.objects.all()
    app_list = [all_apps[i::2] for i in range(2)]
    return render(request, "index.html", context={'apps_list':app_list})



def app_details(request, slug):
    app_detail = Apps.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.app = app_detail
            obj.save()
        return redirect("apps:app_details", slug)
    else:
        form = CommentForm()
    context = {
        "app":app_detail,
        "form": form
    }
    return render(request, "details.html", context)

def vote(request, slug=None):
    if request.method == "POST":
        print(request.POST)
        VoteForm(request.POST).save()
        slug = request.POST['slug']
        app_detail = Apps.objects.get(slug=slug)
        return redirect("apps:app_details", slug)