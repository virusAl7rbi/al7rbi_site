from django.forms import ModelForm
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["name", "content", "email"]

class VoteForm(ModelForm):
    class Meta:
        model = vote
        fields = ["suggestion","vote_up","vote_down"]

class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        fields = ["name", "content", "email"]