# coding: utf-8
from django.db import models
from model_utils.models import TimeStampedModel


class Meeting(TimeStampedModel):
    # user
    # backers
    # rewards
    # updates
    # dynamic fields
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    headline = models.TextField(max_length=140)
    about = models.TextField()
    location = models.TextField()
    when = models.CharField(max_length=255)
    expiration = models.DateTimeField()

    video_url = models.URLField(null=True)
    image_url = models.URLField(null=True)

    visible = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    about_host = models.TextField(null=True)

    min_guests = models.PositiveIntegerField(null=True)
    max_guests = models.PositiveIntegerField(null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('meeting_detail', (), {'slug': self.slug})
