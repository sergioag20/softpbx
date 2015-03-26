# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('user_login')
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


def user_login(request):
    errors = []
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active and user.is_authenticated:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                errors.append('Access denied! User is not active!')
        else:
            errors.append('Access denied! Username or password invalid!')
            return render_to_response('login.html', {'errors': errors, }, context_instance=RequestContext(request))
    else:
        return render_to_response('login.html', context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
