from django.shortcuts import render
from .models import Apps

def apps_list(request):
    all_apps = Apps.objects.all()
    app_list = [all_apps[i::2] for i in range(2)]
    return render(request, "index.html", context={'apps_list':app_list})