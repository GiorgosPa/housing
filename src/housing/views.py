from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.db import IntegrityError
from datetime import datetime
from forms import *


def home(request):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        return redirect('search')
    else:
        return render_to_response('home.html',
                                  RequestContext(request))


def login(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        # Do something for authenticated users.
        pass
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)         
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    log_in(request, user)
                    return redirect('search')
                else:
                    return render_to_response('user_inactive.html',
                                  RequestContext(request))
            return render_to_response('login_fail.html',
                                       c,
                                       RequestContext(request))
    return redirect('search')


def logout(request): 
    log_out(request)
    return redirect('home')


def register(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        # Do something for authenticated users.
        return redirect('search')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                user = authenticate(username=username, password=password)
                log_in(request, user)
                return redirect('search')
            except IntegrityError:
                return render_to_response('user_exists.html',
                                          c,
                                          RequestContext(request))
        else:
            return edirect('home')
