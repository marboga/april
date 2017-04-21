# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages

from django.shortcuts import render, redirect

from .models import Location, Stack
from ..login.models import User

# Create your views here.

def index(request):
    if not 'id' in request.session:
        messages.error(request, 'you must be logged in to visit that page')
        return redirect('auth:index')

    context = {
        'locations': Location.objects.all(),
        'stacks': Stack.objects.all(),
    }
    return render(request, 'location/index.html', context)

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

    return redirect('location:index')

def reset(request):
    request.session.clear()
    return redirect('location:index')


def create(request):
    if request.method == 'POST':
        # print request.POST
        valid, data = Location.objects.validate_and_create(request.POST, request.session['id'])
        print valid, data, "<<<< this was the response back form our function call"

        if valid:
            print "we are successful!"
            #put id into session
        else:
            for err in data:
                messages.error(request, err)

    return redirect('location:index')


def delete(request, id):

    loc = Location.objects.custom_delete_function(id)

def create_stack(request):
    if request.method == 'POST':
        print 'creating stack', request.POST
        if request.POST.get('is_first_stack'):
            is_first_stack = True
        else:
            is_first_stack = False
        new_stack = Stack.objects.create(
            is_first_stack=is_first_stack,
            language=request.POST['language'],
            main_framework=request.POST['main_framework']
        )
        print new_stack.language
    return redirect('location:index')

def add_stack(request):
    print 'adding stack to location'
    Location.objects.add_stack(request.POST)
    return redirect('location:index')

def splash(request):
    return render(request, 'location/splash.html')
