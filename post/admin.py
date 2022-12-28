from django.contrib import admin
from .models import Tweet, TweetLikeDislike, Comment, CommentLikeDislike

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(CommentLikeDislike)
admin.site.register(TweetLikeDislike)