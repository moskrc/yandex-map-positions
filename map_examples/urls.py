from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'example.views.index', name='home'),
    url(r'^map/', include('example.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
