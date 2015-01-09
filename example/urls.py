# -*- coding: utf-8
from django.conf.urls import *

urlpatterns = patterns('example.views',
    url(r'^index/$', 'index', name='index'),
    url(r'^add/$', 'add', name='add'),
    url(r'^edit/(?P<position_id>[0-9]+)/$', 'edit', name='edit'),
)

