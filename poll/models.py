from django.db import models
from django.utils import timezone

class Poll(models.Model):
    auth = models.ForeignKey('auth.User', default=False)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')

    def published(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)