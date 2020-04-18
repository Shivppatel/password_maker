from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'maker/home.html', {'password': 'hasdjfak;jksajf'})

def password(request):
    length = int(request.GET.get('length',12))
    password = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('special_case'):
        chars.extend(list('!@#$%&*_-'))
    if request.GET.get('special_case'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
 
    for _ in range(length):
        password += random.choice(chars)

    return render(request, 'maker/password.html', {'password': password})

def about(request):
    return render(request, 'maker/about.html')