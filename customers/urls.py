"""mobileapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import user_homepage,user_account_login,user_account_logout,user_account_register,user_product_list,user_product_details,add_to_cart,view_mycart,remove_cart_item,cart_order,user_list_all_orders,cancel_order

urlpatterns = [
    path("",user_homepage,name="userhome"),
    path("accountlogin/",user_account_login,name="userlogin"),
    path("accountlogout/",user_account_logout,name="userlogout"),
    path("accountregister",user_account_register,name="userregister"),
    path("products/",user_product_list,name="mobilelist"),
    path("details<int:id>/",user_product_details,name="mobiledetails"),
    path('addtocart/<int:id>',add_to_cart,name="addtocart"),
    path('mycart/',view_mycart,name="mycart"),
    path('removeitem/<int:id>',remove_cart_item,name="removeitem"),
    path('placeorder/<int:id>',cart_order,name="placeorder"),
    path('myorder/',user_list_all_orders,name="myorder"),
    path('cancelorder/<int:id>',cancel_order,name="cancelorder")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

