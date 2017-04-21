# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages

from django.shortcuts import render, redirect

from .models import Location

# Create your views here.

def index(request):
    if not 'id' in request.session:
        messages.error(request, 'you must be logged in to visit that page')
        return redirect('auth:index')

    context = {
        'locations': Location.objects.all()
    }
    response = render(request, 'hello_app/index.html', context)
    response['X-Frame-Options'] = 'DENY'
    response['Content-Security-Policy'] = "frame-ancestors 'none'"
    return response

def show(request, id):
    print id
    return redirect('/')

def name(request):
    if request.method == 'POST':
        #do all our post stuff
        print 'made it to name route'
        print request.POST
        if len(name) > 0:
            request.session['name'] = name
        else:
            messages.error(request, 'your name is too short')
        response = Location.objects.my_custom_method("hi")
        #call function in Models
            #validations
            #call to database
            #return something
        #do something with what is returned

    return redirect('hello_app:index')

def reset(request):
    request.session.clear()
    return redirect('hello_app:index')


def create(request):
    if request.method == 'POST':
        # print request.POST
        valid, data = Location.objects.validate_and_create(request.POST)
        print valid, data, "<<<< this was the response back form our function call"

        if valid:
            print "we are successful!"
            #put id into session
        else:
            for err in data:
                messages.error(request, err)

    return redirect('hello_app:index')


def delete(request, id):

    loc = Location.objects.custom_delete_function(id)
