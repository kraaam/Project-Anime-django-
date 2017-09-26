from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Anime

class IndexView(generic.ListView):
    template_name = 'animeapp/index.html'
    context_object_name = 'all_animes'

    def get_queryset(self):
        return Anime.objects.all()

class DetailView(generic.DetailView):
    model = Anime
    template_name = 'animeapp/detail.html'

class AnimeCreate(CreateView):
    model = Anime
    # initial = {'anime_title': 'woow'}
    fields = ['anime_title', 'anime_sypnosis', 'anime_genre', 'anime_studio', 'anime_logo']

class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['anime_title', 'anime_sypnosis', 'anime_genre', 'anime_studio', 'anime_logo']

class AnimeDelete(DeleteView):
    model = Anime
    success_url = reverse_lazy('anime:index')


