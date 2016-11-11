#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from polls.models import Question
# Create your tests here.
class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		#was_published_recently()遇到未来的时间应该返回False
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date = time)
		self.assertIs(future_question.was_published_recently(), False)
	
	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date = time)
		self.assertIs(recent_question.was_published_recently(), True)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days = 30)
		old_question = Question(pub_date = time)
		self.assertIs(old_question.was_published_recently(), False)
	
class QuestionViewTests(TestCase):
	"""docstring for QuestionViewTests"""
	def test_index_view_with_no_question(self):
		#如果没有问题，显示message
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_with_a_past_question(self):
		#以前的Question应该显示
		create_question(question_text='Past Question.', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question.>'])

	def test_index_view_with_a_future_question(self):
		create_question(question_text='Future Question.', days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_with_future_and_past_question(self):
		create_question(question_text='Future Question.', days=30)
		create_question(question_text='Past Question.', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question.>'])

	def test_index_view_with_two_past_question(self):
		create_question(question_text = 'Past Question1.', days=-30)
		create_question(question_text = 'Past Question2.', days=-31)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
			['<Question: Past Question1.>', '<Question: Past Question2.>'])

class QuestionIndexDetailTest(TestCase):
	"""docstring for QuestionIndexDetailTest"""
	def text_detail_view_with_a_future_question(self):
		future_question = create_question(question_text='Future Question.', days=10)
		url = reverse('polls:detail',args=(future_question.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def text_detail_view_with_a_past_question(self):
		past_question = create_question(question_text='Past Question.', days=-10)
		url = reverse('polls:detail',args=(past_question.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, past_question.question_text)
		
def create_question(question_text,days):
	time = timezone.now() + datetime.timedelta(days = days)		
	return Question.objects.create(question_text = question_text, pub_date = time)
