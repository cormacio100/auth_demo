# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# VIEW TO DISPLAY REGISTER FORM
def register(request):
    if request.method == 'POST':
        #   retrieve values from CUSTOM FORM
        form = UserRegistrationForm(request.POST)
        #   save the form if it is valid
        if form.is_valid():
            form.save()
            #   send flo to authenticate function in backends.py file
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            #   Log the user in and show their profile
            if user:
                login(request,user)
                if request.POST.get('is_entertainer') == 'Yes':
                    messages.success(request, "You have successfully registered as an Entertainer")
                else:
                    messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "unable to log you in at this time!")

    #   IF METHOD NOT EQUAL POST, DISPLAY THE FORM
    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'accounts/register.html', args)


def auth_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        #   if the form is valid lg the user in and return user object
        if form.is_valid():
            #   check if user is authentic
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))
            #    if yes, log them in
            if user is not None:
                auth.login(request, user)
                request.user.last_login = user.last_login
                messages.error(request,"You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None,"Your email or password was not recognised")
    else:
        #   display empty form
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request,'accounts/login.html',args)


def logout(request):
    auth.logout(request)
    messages.success(request,'You have successfully logged out')
    return redirect(reverse('index'))


@login_required(login_url='/login/')
def profile(request):
    #   retrieve the user

    args = {'message': 'Profile loaded', 'last_login': request.user.last_login}
    return render(request, 'accounts/profile.html', args)

