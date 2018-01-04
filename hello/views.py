# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def get_index(request):
    return render(request, 'hello/index.html')


def test_form(request):
    return render(request,'hello/test_form.html')