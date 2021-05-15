from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,CartForm,OrderForm
from django.db.models import Sum
from administrator.models import Mobile
from .models import *
# Create your views here.
def user_homepage(request):
    return render(request,"customers/home.html")

def user_account_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect("userhome")
        else:
            pass
    return render(request, "customers/customerlogin.html")

def user_account_logout(request):
    logout(request)
    return redirect("userlogin")

def user_account_register(request):
    form = UserRegistrationForm()
    context= {}
    context["form"] = form
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            context["form"] = form
            return render(request,"customers/customer_register.html",context)

    return render(request,"customers/customer_register.html",context)

def user_product_list(request):
    mobiles = Mobile.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "customers/productlist.html", context)

def user_product_details(request, id):
    mobile = Mobile.objects.get(id=id)
    context = {}
    context["mobile"] = mobile
    return render(request, "customers/viewproduct.html", context)

# function to get id of each mobile
def get_mobile_object(id):
    return Mobile.objects.get(id=id)

def add_to_cart(request,id):
    if request.user.is_authenticated:
        product=get_mobile_object(id)
        form=CartForm(initial={'user':request.user,'product':product})
        context={}
        context['form']=form
        if request.method=='POST':
            form=CartForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mycart')
            else:
                context['form']=form
                return render(request,'customers/viewproduct.html',context)
        return render(request, 'customers/addtocart.html', context)
    else:
        return redirect("userlogin")

def view_mycart(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        # context= {}
        # context['carts']=carts
        total = Cart.objects.filter(user=request.user).aggregate(Sum('price_total'))
        return render(request, 'customers/viewcart.html', {'carts': carts, 'total': total})
    else:
        return redirect("userlogin")


def remove_cart_item(request,id):
    if request.user.is_authenticated:
        carts = Cart.objects.get(id=id)
        carts.delete()
        return redirect('mycart')
    else:
        return redirect("userlogin")

def cart_order(request,id):
    if request.user.is_authenticated:
        carts=Cart.objects.get(id=id)
        form=OrderForm(initial={'user':request.user,'product':carts.product})
        context={}
        context['form']=form
        if request.method=='POST':
            form=OrderForm(request.POST)
            if form.is_valid():
                form.save()
                remove_cart_item(request,id)
                return redirect('mycart')
            else:
                context['form']=form
                return render(request,'customers/orderitem.html',context)
        return render(request, 'customers/orderitem.html', context)
    else:
        return redirect("userlogin")

def user_list_all_orders(request):
    if request.user.is_authenticated:
        order = Orders.objects.filter(user=request.user)
        context = {}
        context['order'] = order
        return render(request, 'customers/orders.html', context)
    else:
        return redirect("userlogin")

def cancel_order(request,id):
    order=Orders.objects.get(id=id)
    order.status='Cancelled'
    order.save()
    return redirect('myorder')