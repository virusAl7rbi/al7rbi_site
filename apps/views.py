from django.shortcuts import render
from django.http import HttpResponse


def apps(request):
    return render(request, 'index.html')