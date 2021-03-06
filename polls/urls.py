from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    url(r'^add$', views.add, name='add'),
    url(r'^check$', views.check, name='check'),
    url(r'^search$', views.search, name='search'),
    url(r'^searched$', views.searched, name='searched'),
    url(r'^random$', views.get_random, name='get_random'),
    url(r'^faq$', views.get_faq, name='get_faq'),
]