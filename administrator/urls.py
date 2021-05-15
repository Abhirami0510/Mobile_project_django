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

from django.urls import path
from .views import admin_home,admin_login,admin_logout,create_mobile,list_mobiles,update_mobile,delete_mobile,view_mobile,admin_view_order

urlpatterns = [
    path("home",admin_home,name="home"),
    path("",admin_login,name="login"),
    path("logout/",admin_logout,name="logout"),
    path("createmobile/",create_mobile,name="create"),
    path("listmobile/",list_mobiles,name="list"),
    path("delete/<int:id>",delete_mobile,name="delete"),
    path("update/<int:id>",update_mobile,name="update"),
    path("view/<int:id>",view_mobile,name="viewmobile"),
    path("orders/",admin_view_order,name="orders")

]
