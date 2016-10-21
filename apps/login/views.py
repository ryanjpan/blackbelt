from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_date

def index(request):
    context = {
    'users': User.objects.all()
    }
    return render(request, 'login/index.html', context)

def register(request):
    if request.method != 'POST':
        return redirect('/')
    postdata = {
    'name': request.POST['name'],
    'username': request.POST['username'],
    'password': request.POST['pass'],
    'confirm': request.POST['pass2'],
    'datehired': parse_date(request.POST['datehired']),
    }
    result = User.objects.register(postdata)
    print result
    if 'error' in result:
        messages.error(request, result['error'])
    else:
        messages.success(request, 'Successfully added user')
    return redirect('/')

def login(request):
    result = User.objects.login(request.POST['username'], request.POST['pass'])
    if 'error' in result:
        messages.error(request, result['error'])
        return redirect('/')
    user = result['success']
    request.session['name'] = user.name
    request.session['username'] = user.username
    request.session['id'] = user.id
    return redirect(reverse('wishlist:dashboard'))

def logout(request):
    request.session.clear()
    return redirect('/')
