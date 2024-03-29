from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Apps
from datetime import datetime
import json

# apps
class All_apps(generics.ListCreateAPIView):
    serializer_class = AppsSerializer
    queryset = Apps.objects.all()


class app_detail_api(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppsSerializer
    queryset = Apps.objects.all()
    lookup_field = "slug"


@csrf_exempt
@api_view(["POST"])
def github_webhook(request):
    from pprint import pprint
    body = request.body.decode()
    body = json.loads(body)
    data = {
        "updated_time":body['commits'][0]['timestamp'],
        "github_url":body['repository']['url']
    }
    pprint(data)
    app = Apps.objects.get(github_url=data['github_url'])
    app.last_update = datetime.now()
    app.save()
    return Response()


# Commnets
class All_comments(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class app_comments(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    lookup_field = "app_id"


# Suggestion
class All_Suggestion(generics.ListCreateAPIView):
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all()


class app_Suggestion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all()
    lookup_field = "slug"


# vote
class All_votes(generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    queryset = vote.objects.all()


class Suggestion_vote(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VoteSerializer
    queryset = vote.objects.all()
    lookup_field = "suggestion"
