from django.shortcuts import render,redirect
from webapp.models import user,login
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def home(request):  
    return render(request,"home.html")

def public_header(request):  
    return render(request,"public_header.html")

def loginpage(request):  
    return render(request,"loginpage.html")

def userregistration(request):  
    return render(request,"userregistration.html")

def savelogin(request):
    if request.method == 'POST':
        dataa = login.objects.all()
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        flag=0   
        for da in dataa:
            if un == da.username and pwd == da.password:
                type=da.category
                request.session['uid']=un
                flag = 1
                if type=="user":
                      return redirect('/userhome/')
                else:
                    return HttpResponse("Invalid account type")
        if flag==0:
            return HttpResponse("Invalid user")

def saveuser(request):
    if request.method == 'POST':
        data =user()
        data.user_id="na"
        data.name=request.POST.get('name')
        data.email=request.POST.get('email')
        data.address=request.POST.get('address')
        data.phone = request.POST.get('phone')
        data.save()
        data.user_id="user_00"+str(data.id)
        data.save()
        lg=login()
        lg.username=data.user_id
        lg.password=data.phone
        lg.category='user'
        lg.save()
        return redirect('/home')
    else:
        return HttpResponse("Invalid data type")

