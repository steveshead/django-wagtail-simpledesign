from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from blog.models import BlogPage


class HomePage(Page):
    def blogs(self):
        blogs = BlogPage.objects.all()
        blogs = blogs.order_by('-date')[:3]
        return blogs
