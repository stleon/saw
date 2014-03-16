# -*- coding: utf-8 -*-
from django.db import models


class Site(models.Model):
	site = models.CharField('Site', max_length=255, unique=True)
	active = models.BooleanField('Active?', default=True)
	date_created = models.DateTimeField('Created', auto_now_add=True, auto_now=False,)
	date_updated = models.DateTimeField('Updated', auto_now_add=False, auto_now=True,)

	def __unicode__(self):
		return self.site

	class Meta:
		ordering = ['site']


class SiteBaseInformation(models.Model):
	site = models.ForeignKey(Site, verbose_name="Site", related_name="base_info")
	yandex_tyc = models.PositiveIntegerField('Yandex TYC', max_length=6, default=0)
	google_pr = models.PositiveIntegerField('Google PR', max_length=1, default=0)
	# TODO check max
	alexa_all_world = models.PositiveIntegerField('Alexa Rank in all world', max_length=6, default=0)
	alexa_country = models.CharField('Alexa Country', max_length=25, default='none')  # TODO Foreign key to Countries
	# TODO check max
	alexa_rank_in_country = models.PositiveIntegerField('Alexa Rank in country', max_length=6, default=0)
	yandex_blog_links = models.PositiveIntegerField('Yandex Blog link', max_length=9, default=0)
	proindex_google = models.PositiveIntegerField('Proindexirovano v Google', max_length=9, default=0)
	proindex_yandex = models.PositiveIntegerField('Proindexirovano v Yandex', max_length=9, default=0)
	proindex_yandex_popal = models.PositiveIntegerField('Popavshie v index Yandex', max_length=9, default=0)
	yahoo_index = models.PositiveIntegerField('Yahoo index', max_length=9, default=0)
	bing_index = models.PositiveIntegerField('Bing index', max_length=9, default=0)
	bing_outgoing_links = models.PositiveIntegerField('Bing Outgoing Links', max_length=9, default=0)
	# TODO safebrowsing ???
	date_created = models.DateTimeField('Created', auto_now_add=True, auto_now=False,)
	date_updated = models.DateTimeField('Updated', auto_now_add=False, auto_now=True,)

	@classmethod
	def create(cls, **kwargs):
		return cls(**kwargs)

	def __unicode__(self):
		return self.site.site