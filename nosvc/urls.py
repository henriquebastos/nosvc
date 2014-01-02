# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from nosvc.core.views import MeetingCreateView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'nosvc.core.views.home', name='home'),
    url(r'^new/$', MeetingCreateView.as_view(), name='meeting_create'),
    url(r'^(?P<slug>[\w-]+)/$', 'nosvc.core.views.meeting_detail', name='meeting_detail'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^(?P<template_name>.+)$', 'django.shortcuts.render'),
    )
