# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from accounts.models import User

# NESTED TUPLE
STATUS_CHOICES = (
    ('Todo','Todo'),
    ('Doing','Doing'),
    ('Done','Done')
)

class Todo(models.Model):
    """
    Todo model.

    Contains the 'title','description','status' and 'updated' fields
    for a Todo item
    """
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=5,choices=STATUS_CHOICES)
    updated = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title