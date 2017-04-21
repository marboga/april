# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.

class LocationManager(models.Manager):
    def validate_and_create(self, data, id):
        print data, "\n woo we have data"
        errors = []

        if len(data['name']) < 2:
            print "name too short"
            errors.append('name is too short')

        if len(data['street_address']) < 2:
            print "street_address too short"
            errors.append('street address is too short')

        if len(data['city']) < 2:
            print "city too short"
            errors.append('city name is too short')

        if not len(data['state']) == 2:
            errors.append('state abbreviation must be two characters long')

        try:
            zipcode = int(data['zip_code'])
        except:
            errors.append('zip code must be numbers')

        if errors:
            return (False, errors)
        else:
            current_user = User.objects.get(id=id)
            #actually do our database stuff
            new_obj = Location.objects.create(
                name=data['name'],
                street_address=data['street_address'],
                city=data['city'],
                state_abbrev=data['state'],
                zip_code=zipcode,
                captain=current_user
            )

            return (True, new_obj)

    def custom_delete_function(self, id):
        # all validations go here
        #if logged in user has permissions to do so:
            # delete
        # else:
            # return errors
        # don't touch the db unless all validations
        pass

    def add_stack(self, data):
        print data
        try:
            location = self.get(id=data['location'])
            stack = Stack.objects.get(id=data['stack'])
            location.stacks_offered.add(stack)
            location.save()
            print 'all is well'
        except:
            print 'error happened'




# class Employee(models.Model):
#     user = models.OneToOneField(User)
#     is_active = models.BooleanField()
#     hire_date = models.DateTimeField()
#     location = models.ForeignKey(Location, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



class Stack(models.Model):
    language = models.CharField(max_length=255)
    main_framework = models.CharField(max_length=255)
    is_first_stack = models.BooleanField()
    # category = models.ForeignKey(Category, related_name='stacks_in_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_abbrev = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    captain = models.OneToOneField(User, null=True)
    stacks_offered = models.ManyToManyField(Stack, related_name='available_locations')

    objects = LocationManager()
