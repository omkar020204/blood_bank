from django.shortcuts import render,redirect
from donate.models import Donor
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
            qty=request.POST.get('qty',0)
            bg=request.POST.get('bg','')
            bgg={'bloodGrp':bg}
            blood=Donor.objects.values('bloodGrp','aadhar','donationDate')
            temp=int(0)
            target=int(qty)
            for i in blood:
               if bgg['bloodGrp']==i['bloodGrp']:
                  temp=temp+1
            if temp>=target:
               count=int(0)
               for i in blood :
                  if i['bloodGrp']==bg:
                     if count<temp:
                     #   print(temp)
                        tpp=i['aadhar']
                        cpp=i['donationDate']
                        dell=Donor.objects.get(donationDate=cpp,aadhar=tpp)
                        dell.delete()
                        print(dell)
                        count+=1
                     #   print(count)
                     else:
                        break
                     return redirect('buy:success')
            else:
               return redirect('buy:fail')
    else:  
       return render(request,'buy/index.html')
# Create your views here.
def success(request):
   return render(request,'buy/success.html')
def fail(request):
   return render(request,'buy/fail.html')