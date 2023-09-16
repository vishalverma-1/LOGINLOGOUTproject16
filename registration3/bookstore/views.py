from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .models import book
def myfun(request):
    if request.method=='POST':
      name=request.POST.get('name')
      mobile=request.POST.get('mobile')
      password=request.POST.get('password')
      confirm_password=request.POST.get('confirm_password')
      obj=book.objects.create(name=name,mobile=mobile,password=password)
      if password==confirm_password:
         obj.save()
         return redirect('login')
      else:
         return HttpResponse("invlid credentials") 
    else:
         return render(request,'book.html')


#---------LOGIN---------------

def login(request):
   if request.method=='POST':
      name=request.POST.get('name')
      password=request.POST.get('password')
      obj=book.objects.get(name=name,password=password)
      if(obj is not None):
         return redirect('mypage')
   else:
        return render(request,'login.html')  
         
#------------SHOW MY WEBSITE AFTER LOGIN--------------
def mypage(request):
   return render(request,'mypage.html')


#--------------LOGOUT MY WEBSITE PAGE-----------------
def logout(request):
   auth.logout(request)
   return redirect('login')


