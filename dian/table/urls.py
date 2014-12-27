#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from table import views


urlpatterns = [
    url(r'^table-type/$', views.TableTypeList.as_view()),
    url(r'^table-type/(?P<pk>[0-9]+)/$', views.TableTypeDetail.as_view()),

    url(r'^table/$', views.TableList.as_view()),
    url(r'^table/(?P<pk>[0-9]+)/$', views.TableDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

