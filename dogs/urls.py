from django.conf.urls import (patterns, url)
from dogs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<owner_id>\d+)/$', views.dog_detail, name='dog_detail'),
)
