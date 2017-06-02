# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page, Section

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	inlines = [SectionInline]


admin.site.register(Page, PageAdmin)