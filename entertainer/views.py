# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import EntertainerRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_profile(request):
    if request.method == 'POST':
        #   user bject is passed to the form class constructor
        form = EntertainerRegistrationForm(request.user,request.POST)
        if form.is_valid():
            #form.user = request.user
            form.save()
            args = {'message': 'Entertainer listing created'}
            return render(request, 'entertainer/profile_created.html',args)
    else:
        #   When the form is loaded initially
        #   must pass the newly created user object to it's constructor
        form = EntertainerRegistrationForm(request.user)
        return render(request, 'entertainer/create_profile.html', {'form': form})