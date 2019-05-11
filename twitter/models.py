from django.db import models
from django.contrib.auth.models import User


TWITTER_MAXIMUM_TWEET_LENGTH = 140
TWITTER_MAXIMUM_COMMENT_LENGTH = 60
TWITTER_MAXIMUM_MSG_LENGTH = 64


class Tweet(models.Model):
    content = models.CharField(max_length=TWITTER_MAXIMUM_TWEET_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] TWEET by {}: {}'.format(
            self.creation_date,
            self.user, self.content[:20])

