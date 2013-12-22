# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'nosvc.core.views.home', name='home'),
    url(r'^(?P<slug>[\w-]+)/$', 'nosvc.core.views.meeting_detail', name='meeting_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
