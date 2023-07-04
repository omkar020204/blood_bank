from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.urls import include
def index(request):
    if request.method=='POST':
        if 'buy' in request.POST:
            return redirect('buy:home')
        elif 'donate' in request.POST:
            return redirect('donate:home')
        elif 'history' in request.POST:
            return redirect('history:home')
        elif 'camp' in request.POST:
            return redirect('camp:home')
        elif 'register' in request.POST:
            return redirect('register:home')
        elif 'home' in request.POST:
            return redirect('home')
    return render(request,'blooddonation/index.html')
