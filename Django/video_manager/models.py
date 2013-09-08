from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Surgeon(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Video(models.Model):
    filename = models.CharField(max_length=200)
    task = models.ForeignKey(Task)
    surgeon = models.ForeignKey(Surgeon)

    def __unicode__(self):
        return self.filename + " | " + self.task.name + " | By: " + self.surgeon.name

class Rating(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    rating = models.IntegerField(max_length=5, choices=[(i, i) for i in range(1,6)])

    def __unicode__(self):
        return self.user.username + "'s Rating for " + self.video.filename + " - " + str(self.rating)