from django.shortcuts import render, redirect
from buyer.models import *
from siteadmin.models import *
from seller.models import *
from django.contrib import messages
import datetime

def register_buyer(request):
    return render(request, 'register_buyer.html')
def register_buyer_action(request):
    nam=request.POST['name']
    add=request.POST['address']
    gen=request.POST['gender']
    dob=request.POST['dob']
    pho=request.POST['phone']
    cou=request.POST['country']
    use=request.POST['username']
    pas=request.POST['password']
    g=register_tb(Name=nam,Address=add,Gender=gen,Dob=dob,Phone=pho,Country=cou,Username=use,Password=pas)
    g.save()
    return redirect('register_buyer')
def updatebuyer(request):
    buy=request.session['id']
    buyer=register_tb.objects.filter(id=buy)
    return render(request, 'updatebuyer.html', {'buy':buyer})
def updatebuyeraction(request):
    buy=request.session['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(id=buy).update(Name=name,Address=address,Gender=gender,Dob=dob,Phone=phone,Country=country,Username=username,Password=password)
    return redirect('updatebuyer')
def viewsellerproducts(request):
    product=product_tb.objects.all()
    return render(request, 'viewsellerproducts.html', {'pro':product})
def addtocart(request,id):
    product=product_tb.objects.filter(id=id)
    return render(request, 'addtocart.html', {'pro':product})
def addtocartaction(request):
    buyer=request.session['id']
    product=request.POST['productid']
    name=request.POST['name']
    shipping=request.POST['shippingaddress']
    phone=request.POST['phone']
    quantity=request.POST['quantity']
    totalprice=request.POST['totalprice']
    user=cart_tb(Name=name,Shipping_address=shipping,Phone=phone,Quantity=quantity,Total_price=totalprice,Buyerid_id=buyer,Productid_id=product)
    user.save()
    return redirect('viewsellerproducts')

def viewcart(request):
    buyer=request.session['id']
    cart=cart_tb.objects.filter(Buyerid=buyer)
    return render(request, 'viewcart.html',{'cart':cart})
def deletecart(request, id):
    carts=cart_tb.objects.filter(id=id).delete()
    return redirect('viewcart')
def placeorderaction(request):
    checkbox=request.POST.getlist('checkbox')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    for c in checkbox:
        cop=cart_tb.objects.filter(id=c)
        shippingaddress=cop[0].Shipping_address
        quantity=cop[0].Quantity
        stock=cop[0].Productid.stock
        phone=cop[0].Phone
        totalprice=cop[0].Total_price
        buyer=request.session['id']
        product=cop[0].Productid
        seller=cop[0].Productid.seller
        if quantity >int(stock):
            messages.add_message(request, messages.INFO, 'quantity is higher')
            return redirect('viewcart')
        else:
            order=order_tb(shippingaddress=shippingaddress,quantity=quantity,phone=phone,stock=stock,totalprice=totalprice,date=date,time=time,buyerid_id=buyer,productid=product,sellerid=seller)
            order.save()
            newstock=int(stock)-quantity
            pro=product_tb.objects.filter(id=product.id).update(stock=newstock)
            cop.delete()
    return redirect('viewcart')
def ordersofbuyer(request):
    buyer=request.session['id']
    order=order_tb.objects.filter(buyerid=buyer)
    return render(request, 'ordersofbuyer.html', {'order':order})
def cancelorder(request, id):
    order=order_tb.objects.filter(id=id).update(Status='cancelled')
    return redirect('ordersofbuyer')
def trackingforbuyer(request, id):
    track=tracking_tb.objects.filter(orderid=id)
    return render(request, 'trackingforbuyer.html', {'track':track})
def logout(request):
    buyer=request.session.flush()
    return redirect('index')
def searchbyproduct(request):
    return render(request, 'searchbyproduct.html')
def searchbyproductaction(request):
    product=request.POST['product']
    pro=product_tb.objects.filter(product__istartswith=product)
    return render(request, 'viewsellerproducts.html', {'pro':pro})
def searchbycategory(request):
    cat=Category_tb.objects.all()
    return render(request, 'searchbycategory.html', {'cat':cat})
def searchbycategoryaction(request):
    category=request.POST['category']
    price=request.POST['price']
    p=product_tb.objects.filter(price__gte=price, category_id=category)
    return render(request, 'viewsellerproducts.html', {'pro':p})

    

# Create your views here.
