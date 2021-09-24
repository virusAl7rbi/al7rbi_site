from django.forms import ModelForm
from .models import Comments, vote

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["name", "content", "email"]

class VoteForm(ModelForm):
    class Meta:
        model = vote
        fields = ["comment","vote_up","vote_down"]