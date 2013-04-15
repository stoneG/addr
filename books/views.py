from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from models import Addresses

def main(request):
    errors = []
    if request.method == 'POST' and isinstance(request.user, User):
        required = ['name', 'line_one', 'city', 'state', 'zip_code']
        for entry in required:
            if not request.POST.get(entry, ''):
                errors.append(entry)
        if not errors:
            new_addr = Addresses(name=request.POST['name'],
                                 line_one=request.POST['line_one'],
                                 line_two=request.POST['line_two'],
                                 city=request.POST['city'],
                                 state=request.POST['state'],
                                 zip_code=request.POST['zip_code'],
                                 user=User.objects.get(username=request.user)).save()
    elif request.method == 'POST':
        errors.append('Please log in')
    if isinstance(request.user, User):
        addresses = Addresses.objects.filter(user=request.user)
    else:
        addresses = []
    return render(request, 'main.html', {'addresses': addresses, 'errors': errors})

def log_in(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                # NOTE: May want to do acct deactivations later
                login(request, user)
            return HttpResponseRedirect('/')
        else:
            if User.objects.filter(username=email):
                error = 'The password given does not match the one our records.'
            else:
                error = 'There is no account associated with that email address.'
            return render(request, 'login.html', {'error': error})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if request.user.is_authenticated():
            return HttpResponseBadRequest()
        if user is not None:
            if user.is_active:
                login(request, user)
            return HttpResponseRedirect('main')
        else:
            if User.objects.filter(username=email):
                error = 'The password given does not match the one our records.'
            else:
                error = 'There is no account associated with that email address.'
            return HttpResponseRedirect(request, 'login.html', {'error': error})
