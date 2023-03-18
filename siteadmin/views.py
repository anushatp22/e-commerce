from django.shortcuts import render, redirect
from siteadmin.models import *
from buyer.models import *
from seller.models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def loginaction(request):
    user=request.POST['username']
    password=request.POST['password']
    admin=user_tb.objects.filter(Username=user, Password=password)
    buyer=register_tb.objects.filter(Username=user,Password=password)
    seller=register_seller_tb.objects.filter(Username=user,Password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request, 'home.html')
    elif buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request, 'home_buyer.html')
    elif seller.count()>0:
        status=seller[0].Status
        request.session['id']=seller[0].id
        if status=='approved':
            return render(request, 'home_seller.html')
        else:
            return redirect('login') 
    else:
        return redirect('login')
def viewregisteredseller(request):
    seller=register_seller_tb.objects.all()
    return render(request, 'viewregisteredseller.html', {'sell':seller})
def approve(request,id):
    seller=register_seller_tb.objects.filter(id=id).update(Status='approved')
    return redirect('viewregisteredseller')
def category(request):
    return render(request, 'category.html')
def categoryaction(request):
    category=request.POST['category']
    add=Category_tb(Items=category)
    add.save()
    return redirect('category')
def logout(request):
    admin=request.session.flush()
    return redirect('index')
def forgotpassword(request):
    return render(request, 'forgotpassword.html')
def forgotpasswordaction(request):
    username=request.POST['username']
    buyer=register_tb.objects.filter(Username=username)
    seller=register_seller_tb.objects.filter(Username=username)
    if buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request, 'newpassword.html', {'data':username})
    elif seller.count()>0:
        request.session['id']=seller[0].id
        return render(request, 'newpassword.html', {'data':username})
    else:
        return redirect('login')
def newpasswordaction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    username=request.POST['username']
    buyer=register_tb.objects.filter(Name=name,Dob=dob,Username=username)
    seller=register_seller_tb.objects.filter(Name=name,Dob=dob, Username=username)
    if buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request, 'enterpassword.html', {'data':username})
    elif seller.count()>0:
        request.session['id']=seller[0].id
        return render(request, 'enterpassword.html', {'data':username})
    else:
        return redirect('login')
def enterpasswordaction(request):
    password=request.POST['password']
    confirm=request.POST['cofirm']
    username=request.POST['username']
    if password == confirm:
        buyer=register_tb.objects.filter(Username=username)
        seller=register_seller_tb.objects.filter(Username=username)
        if buyer.count()>0:
            request.session['id']=buyer[0].id
            bu=request.session['id']
            b=register_tb.objects.filter(id=bu).update(Password=password)
        else:
            seller.count()>0
            request.session['id']=seller[0].id
            se=request.session['id']
            s=register_seller_tb.objects.filter(id=se).update(Password=password)
        request.session.flush()
        return redirect('login')
    else:
        return redirect('forgotpasswordaction')
            


        
# Create your views here.
