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
        fields = ["name", "content", "email", "created_at", "app", "votes"]


class AppsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)
    suggestions = SuggestionSerializer(many=True)

    class Meta:
        model = Apps
        fields = [
            "name",
            "description",
            "web_url",
            "ios_url",
            "android_url",
            "desk_win_url",
            "desk_mac_url",
            "desk_lin_url",
            "image",
            "last_update",
            "published_time",
            "platforms",
            "slug",
            "comments",
            "suggestions",
        ]
