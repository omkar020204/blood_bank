from django.shortcuts import render,redirect
from donate.models import Donor2
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
        else:
            aadharr=request.POST.get('aadhar','')
            prod=Donor2.objects.filter(aadhar=aadharr)
            print(prod)
            param={'list':prod}
            return render(request,'history/result.html',param)
    return render(request,'history/index.html')
def result(request):
    return render(request,'history/result.html')
# Create your views here.
