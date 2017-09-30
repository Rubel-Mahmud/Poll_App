from django.conf.urls import url
from . import views

app_name = 'poll'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>[0-9]+)/detail$', views.detail, name='detail'),
    url(r'^(?P<poll_id>[0-9]+)/vote$', views.vote, name='vote'),
    url(r'^(?P<poll_id>[0-9]+)/result$', views.result, name='result'),
]