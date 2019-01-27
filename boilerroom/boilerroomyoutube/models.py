from django.db import models


class YoutubeVideo(models.Model):
    url = models.TextField("url", null=False, blank=False)
