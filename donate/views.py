from django.shortcuts import render,redirect
from.models import Donor,Donor2
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
            # request.method=='POST':
            name=request.POST.get('name','#')
            address=request.POST.get('address1','')
            bloodGrp=request.POST.get('bg','')
            mobile=request.POST.get('mobile','')
            dob=request.POST.get('dob','')
            aadhar=request.POST.get('aadhar','')
            donationdate=request.POST.get('donationdate','')
            donor=Donor(name=name,address=address,contact=mobile,bloodGrp=bloodGrp,dob=dob,aadhar=aadhar,donationDate=donationdate)
            donor2=Donor2(name=name,address=address,contact=mobile,bloodGrp=bloodGrp,dob=dob,aadhar=aadhar,donationDate=donationdate)
            donor.save()
            donor2.save()
            return render(request,'donate/thanks.html')
    return render(request,'donate/index.html')
def thanks(request):
    return render(request,'donate/thanks.html')
# Create your views here.
