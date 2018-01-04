# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import User
from django.db import models


# Create your models here.
class Entertainer(models.Model):
    #   DEFINE CHOICES LISTS WITH CONSTANTS
    ENT_TYPES = (
        ('Band', 'Band'),
        ('Solo', 'Solo')
    )
    GENRE_TYPES = (
        ('Rock', 'Rock'),
        ('Metal', 'Metal'),
        ('Punk', 'Punk'),
        ('Blues', 'Blues'),
        ('Jazz', 'Jazz'),
        ('Classical', 'Classical'),
        ('Reggae', 'Reggae'),
        ('Ska', 'Ska'),
        ('Dance', 'Dance'),
        ('Electronic', 'Electronic'),
        ('Folk', 'Folk'),
        ('Pop', 'Pop'),
        ('Funk', 'Funk'),
        ('Trad', 'Trad'),
        ('Country', 'Country'),
        ('Soul', 'Soul'),
        ('RnB','RnB'),
        ('Other', 'Other'),
    )

    #   An Entertainer is a User - One To One Relationship
    user = models.OneToOneField(User,
                                related_name='user')
    #   FIELDS
    title = models.CharField(
        max_length = 15
    )
    description = models.CharField(
        max_length = 14,
        choices = ENT_TYPES,
        default = 'Band'
    )
    genre = models.CharField(
        max_length = 11,
        choices = GENRE_TYPES,
        default = 'Rock'
    )
    profileImage = models.ImageField(
        upload_to = 'entertainers/media/images/profile/',
        default='media/no_image.png'
    )