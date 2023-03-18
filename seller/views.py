from django.shortcuts import render, redirect
from seller.models import *
from siteadmin.models import *
from buyer.models import *
from django.contrib import messages
import datetime

def register_seller(request):
    return render(request, 'register_seller.html')
def register_seller_action(request):
    nam=request.POST['name']
    add=request.POST['address']
    dob=request.POST['dob']
    gen=request.POST['gender']
    pho=request.POST['phone']
    cou=request.POST['country']
    use=request.POST['username']
    pas=request.POST['password']
    if len(request.FILES)>0:
        ima=request.FILES['image']
    else:
        ima='no pic'
    user=register_seller_tb(Name=nam,Address=add,Dob=dob,Gender=gen,Phone=pho,Country=cou,Username=use,Password=pas,Image=ima)
    user.save()
    return redirect('register_seller')
def update_seller(request):
    seller=request.session['id']
    sell=register_seller_tb.objects.filter(id=seller)
    return render(request, 'update_seller.html', {'se':sell})
def update_seller_action(request):
    sellerid=request.session['id']
    seller=register_seller_tb.objects.filter(id=sellerid)
    nam=request.POST['name']
    add=request.POST['address']
    dob=request.POST['dob']
    gen=request.POST['gender']
    pho=request.POST['phone']
    cou=request.POST['country']
    use=request.POST['username']
    pas=request.POST['password']
    if len(request.FILES)>0:
        ima=request.FILES['image']
    else:
        ima=seller[0].Image
    hu=register_seller_tb.objects.filter(id=sellerid).update(Name=nam,Address=add,Dob=dob,Gender=gen,Phone=pho,Country=cou,Username=use,Password=pas)
    seller_object=register_seller_tb.objects.get(id=sellerid)
    seller_object.Image=ima
    seller_object.save()
    return render(request, 'home_seller.html')
def add_product(request):
    category=Category_tb.objects.all()
    return render(request, 'add_product.html', {'cat':category})
def add_product_action(request):
    seller=request.session['id']
    product=request.POST['product']
    price=request.POST['price']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image='no pic'
    details=request.POST['details']
    stock=request.POST['stock']
    category=request.POST['category']
    user=product_tb(seller_id=seller,product=product,price=price,image=image,details=details,stock=stock,category_id=category)
    user.save()
    return redirect('add_product')
def viewproduct(request):
    seller1=request.session['id']
    product=product_tb.objects.filter(seller=seller1)
    return render(request, 'viewproduct.html', {'pro':product})
def editproducts(request, id):
    category=Category_tb.objects.all()
    product=product_tb.objects.filter(id=id)
    return render(request, 'editproducts.html', {'pro':product, 'cat':category})
def editproductsaction(request):
    seller=request.session['id']
    productid=request.POST['productid']
    product=product_tb.objects.filter(id=productid)
    products=request.POST['product']
    price=request.POST['price']
    details=request.POST['detail']
    stock=request.POST['stock']
    category=request.POST['category']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image=product[0].image
    user=product_tb.objects.filter(id=productid).update(product=products,details=details,price=price,stock=stock,category_id=category,seller_id=seller)
    product_objects=product_tb.objects.get(id=productid)
    product_objects.image=image
    product_objects.save()
    return redirect('viewproduct')
def deleteproduct(request, id):
    uer=product_tb.objects.filter(id=id).delete()
    return redirect('viewproduct')
def viewbuyerorders(request):
    seller=request.session['id']
    order=order_tb.objects.filter(sellerid=seller)
    return render(request, 'viewbuyerorders.html', {'order':order})
def approveorder(request, id):
    approve=order_tb.objects.filter(id=id).update(Status='approved')
    return redirect('viewbuyerorders')
def rejectorder(request, id):
    order=order_tb.objects.filter(id=id).update(Status='rejected')
    return redirect('viewbuyerorders')
def trackingdetails(request, id):
    order=order_tb.objects.filter(id=id)
    return render(request, 'trackingdetails.html', {'order':order})
def trackingdetailsaction(request):
    orderid=request.POST['id']
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    track=tracking_tb(details=details, date=date,time=time,orderid_id=orderid)
    track.save()
    return redirect('viewbuyerorders')
def confirmcancel(request, id):
    order=order_tb.objects.filter(id=id).update(Status='confirm cancel')
    return redirect('viewbuyerorders')
def logout(request):
    seller=request.session.flush()
    return redirect('index')
    


    

# Create your views here.
