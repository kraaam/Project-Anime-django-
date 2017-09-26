from django.db import models
from django.core.urlresolvers import reverse


class Anime(models.Model):
    anime_title = models.CharField(max_length=500)
    anime_sypnosis = models.CharField(max_length=3000)
    anime_genre = models.CharField(max_length=350)
    anime_studio = models.CharField(max_length=500)
    anime_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('anime:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.anime_title + '-' + self.anime_genre + '-' + self.anime_logo

