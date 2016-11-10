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
		url(r'^$', views.index, name='index'),
		url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
		url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
		url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]

