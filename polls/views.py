#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
# Create your views here.

def index(request):
	'''
	#硬编码
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
	'''
	'''
	#使用loader + HttpResponse
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))
	'''
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})	

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question':question,
			'error_message':u"您未选择！",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#成功处理POST数据后一定要返回HttpResponseReditect,防止用户后退后POST两次数据
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))	




