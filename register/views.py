from django.shortcuts import render,redirect
from register.models import Login,Form
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
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            arr=Login.objects.values('username','password')
            for i in arr:
                if i['username']==username and i['password']==password:
                    return redirect('register:form')
    return render(request,'register/index.html')
def form(request):
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
                time=request.POST.get('time1',"00:00")
                address=request.POST.get('address1','')
                date=request.POST.get('date1','2001-01-01')
                login=Form(time=time,address=address,date=date)
                login.save()
                return render(request,'register/done.html')
        return render(request,'register/form.html')
# Create your views here.
