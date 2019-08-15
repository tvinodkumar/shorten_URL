from django.db import models


class Shorten_URLS(models.Model):
    shorten_url = models.CharField(max_length=50)
    url_name = models.CharField(max_length=250)

    def __str__(self):
        return self.shorten_url
