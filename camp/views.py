from django.shortcuts import render,redirect
from register.models import Form
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
    arr=Form.objects.values('address','time','date')
    n=len(arr)
    param={'allcamps':arr}
    return render(request,'camp/index.html',param)
# Create your views here.
