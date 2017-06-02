# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models

class Page(models.Model):
	title = models.CharField(max_length=250, unique=True, blank=False)
	slug = models.SlugField(unique=True)
	body = tinymce_models.HTMLField()
	published = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('page.views.details', args=[str(self.id)])

class Section(models.Model):
	heading = models.CharField(max_length=250, unique=True, blank=True)
	slug = models.SlugField(unique=True, blank=True)
	body = models.TextField(blank=True)
	page = models.ForeignKey(Page)

	def __unicode__(self):
		return self.title

	

