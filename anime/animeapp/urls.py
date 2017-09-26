from django.conf.urls import url
from . import views

app_name ='anime'

urlpatterns =[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'add/$', views.AnimeCreate.as_view(), name='anime-add'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AnimeUpdate.as_view(), name='anime-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AnimeDelete.as_view(), name='anime-delete'),

]