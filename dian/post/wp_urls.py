# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns(
    'post.wp_views',

    url(r'^list-post/$', 'list_post'),
    url(r'^create-post/$', 'create_post'),
    url(r'^get-post/(?P<pk>[0-9]+)/$', 'get_post'),
    url(r'^update-post/(?P<pk>[0-9]+)/$', 'update_post'),

    url(r'^list-tag-with-restaurant/(?P<restaurant_openid>\w+)/$', 'list_tag_with_restaurant'),
    url(r'^create-tag/$', 'create_tag'),
    url(r'^get-tag/(?P<pk>[0-9]+)/$', 'get_tag'),
    url(r'^update-tag/(?P<pk>[0-9]+)/$', 'update_tag'),
)
