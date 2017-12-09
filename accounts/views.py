# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from django.http import HttpResponse


#   Used by REST for authentication
class UserView(APIView):
    """
    UserView handles the requests made to "/accounts/"
    """

    #   permissions set to allow all users acces
    permission_classes = ()


    def post(self,request):
        """
        Handles the POST request made to the '/accounts/' URL

        This view will take the 'data' property from the 'request'
        object, desrialize it into a 'User' object and store in the DB

        Returns a 201 (successfully created) if the user is successfully
        created. Otherwise returns a 400 (bad request)

        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)

        # Check to see if the data in the 'request' is valid
        # If they cannot be desrialized into a User object then
        # a bad request response will be returned
        # Else, save the data and return the data and a
        # sucessfully created status
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            # Create a new user using the 'username' contained in
            # the 'data' dict
            user = User.objects.create(username=data["username"])
            # Use the 'set password' method to create a hashed password
            # using the data provided in the 'data dict
            user.set_password(data['password'])
            # Finally, save the new 'user' object
            user.save()
            return Response(data, status=status.HTTP_201_CREATED)


# VIEW TO DISPLAY REGISTER FORM
def auth_register(request):
    #return HttpResponse("Register Page")
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
                    return redirect(reverse('entertainer:create_profile'))
                else:
                    messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "unable to log you in at this time!")

        args = {'message':'Method is POST'}
        #return render(request, 'accounts/test.html',{'message':'Method is POST'})
    #   IF METHOD NOT EQUAL POST, DISPLAY THE FORM
    else:
        args = {'message': 'Method is GET'}
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'accounts/register.html', args)
    #return render(request, 'accounts/test.html',args)

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
    return render(request, 'accounts/login.html', args)


@login_required(login_url='/login/')
def auth_logout(request):
    auth.logout(request)
    messages.success(request,'You have successfully logged out')
    return redirect(reverse('index'))


@login_required(login_url='/login/')
def auth_profile(request):
    #   retrieve the user

    args = {'message': 'Profile loaded', 'last_login': request.user.last_login}
    return render(request, 'accounts/profile.html', args)


def test(request):
    return HttpResponse("Test Page")