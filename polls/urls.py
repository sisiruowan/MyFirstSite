#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-09 20:26:29
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com
'''
	description: 
'''

from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
		#上一级匹配到了 polls/, 把剩下的传到了这里
		url(r'^$', views.IndexView.as_view(), name='index'),
		url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
		url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name='results'),
		url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]

