from django.db import models


class YoutubeVideo(models.Model):
    url = models.TextField("url", null=False, blank=False)
    etag = models.TextField("etag", null=False, blank=False)
    title = models.TextField("title", null=False, blank=False)
    published_at = models.DateTimeField("published_at", null=False, blank=False)
    channel_id = models.TextField("channel_id", null=False, blank=False)
