from django.contrib import admin
from .models import Apps, Comments, vote, Suggestion

admin.site.register(Apps)
admin.site.register(Comments)
admin.site.register(vote)
admin.site.register(Suggestion)
