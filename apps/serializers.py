from rest_framework import serializers
from .models import Apps, Comments, Suggestion, vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = vote
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class SuggestionSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True)

    class Meta:
        model = Suggestion
        exclude = ()


class AppsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)
    suggestions = SuggestionSerializer(many=True)

    class Meta:
        model = Apps
        exclude = ()