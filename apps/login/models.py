from __future__ import unicode_literals

from django.db import models

import bcrypt

class UserManager(models.Manager):
    def login(self, username, password):
        if len(username) < 3:
            return {'error': 'Username Invalid'}
        try:
            user = User.objects.get(username=username)
        except:
            return {'error': 'Username not found'}
        pword = user.password.encode('utf-8')
        password = password.encode('utf-8')
        if not bcrypt.hashpw(password, pword) == pword:
            return {'error': 'Password does not match'}
        return {'success': user}
    def register(self, postdata):
        username = postdata['username']
        try:
            User.objects.get(username=username)
            return {'error': 'This username already exists'}
        except:
            pass
        if len(username) < 3:
            return {'error': 'Username must be longer than 3'}
        name = postdata['name']
        if len(name) < 3 or not name.isalpha:
            return {'error': 'First Name must be letters and longer than 3'}
        datehired = postdata['datehired']
        pword = postdata['password']
        if len(pword) < 8:
            return {'error': 'Password Invalid'}
        pword2 = postdata['confirm']
        if pword != pword2:
            return {'error': 'Passwords don\'t match'}
        pword = pword.encode('utf-8')
        hashpw = bcrypt.hashpw(pword, bcrypt.gensalt())
        User.objects.create(name=name, username=username, password=hashpw, date_hired=datehired)
        return {'user':User.objects.get(username=username)}



class User(models.Model):
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=100)
    date_hired = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
