# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.
class Post(models.Model):
    """
    Attributes:
        -   Title
        -   Creation Date
        -   Published Date
        -   Post Content
        -   Author
    """
    #   author is linked to a registered user
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True,null=True)

    #   When we decide to publish the blog entry,
    #   our publish function can be
    #   called to update the database
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #   display entries by title on the Admin page
    def __unicode__(self):
        return self.title
