"""onlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views as adminview
from buyer import views as buyerview
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adminview.index, name='index'),
    path('login/', adminview.login, name='login'),
    path('loginaction/', adminview.loginaction, name='loginaction'),
    path('register_buyer/', buyerview.register_buyer, name='register_buyer'),
    path('register_buyer_action/', buyerview.register_buyer_action, name='register_buyer_action'),
    path('register_seller/', sellerview.register_seller, name='register_seller'),
    path('register_seller_action/', sellerview.register_seller_action, name='register_seller_action'),
    path('update_seller/', sellerview.update_seller, name='update_seller'),
    path('update_seller_action/', sellerview.update_seller_action, name='update_seller_action'),
    path('viewregisteredseller/', adminview.viewregisteredseller, name='viewregisteredseller'),
    path('approve<int:id>/', adminview.approve, name='approve'),
    path('add_product/', sellerview.add_product, name='add_product'),
    path('category/', adminview.category, name='category'),
    path('categoryaction/', adminview.categoryaction, name='categoryaction'),
    path('add_product_action/', sellerview.add_product_action, name='add_product_action'),
    path('viewproduct/', sellerview.viewproduct, name='viewproduct'),
    path('editproducts<int:id>/', sellerview.editproducts, name='editproducts'),
    path('editproductsaction/', sellerview.editproductsaction, name='editproductsaction'),
    path('deleteproduct<int:id>/', sellerview.deleteproduct, name='deleteproduct'),
    path('updatebuyer/', buyerview.updatebuyer, name='updatebuyer'),
    path('updatebuyeraction/', buyerview.updatebuyeraction, name='updatebuyeraction'),
    path('viewsellerproducts/', buyerview.viewsellerproducts, name='viewsellerproducts'),
    path('addtocart<int:id>/', buyerview.addtocart, name='addtocart'),
    path('addtocartaction/', buyerview.addtocartaction, name='addtocartaction'),
    path('viewcart/', buyerview.viewcart, name='viewcart'),
    path('deletecart<int:id>/', buyerview.deletecart, name='deletecart'),
    path('placeorderaction/', buyerview.placeorderaction, name='placeorderaction'),
    path('viewbuyerorders/', sellerview.viewbuyerorders, name='viewbuyerorders'),
    path('ordersofbuyer/', buyerview.ordersofbuyer, name='ordersofbuyer'),
    path('cancelorder<int:id>/', buyerview.cancelorder, name='cancelorder'),
    path('approveorder<int:id>/', sellerview.approveorder, name='approveorder'),
    path('rejectorder<int:id>/', sellerview.rejectorder, name='rejectorder'),
    path('trackingdetails<int:id>/', sellerview.trackingdetails, name='trackingdetails'),
    path('trackingdetailsaction/', sellerview.trackingdetailsaction, name='trackingdetailsaction'),
    path('trackingforbuyer<int:id>/', buyerview.trackingforbuyer, name='trackingforbuyer'),
    path('confirmcancel<int:id>/', sellerview.confirmcancel, name='confirmcancel'),
    path('logout/', adminview.logout, name='logout'),
    path('logout/', buyerview.logout, name='logout'),
    path('logout/', sellerview.logout, name='logout'),
    path('forgotpassword/', adminview.forgotpassword, name='forgotpassword'),
    path('forgotpasswordaction/', adminview.forgotpasswordaction, name='forgotpasswordaction'),
    path('newpasswordaction/', adminview.newpasswordaction, name='newpasswordaction'),
    path('enterpasswordaction/', adminview.enterpasswordaction, name='enterpasswordaction'),
    path('searchbyproduct/', buyerview.searchbyproduct, name='searchbyproduct'),
    path('searchbyproductaction/', buyerview.searchbyproductaction, name='searchbyproductaction'),
    path('searchbycategory/', buyerview.searchbycategory, name='searchbycategory'),
    path('searchbycategoryaction/', buyerview.searchbycategoryaction, name='searchbycategoryaction')
       
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
