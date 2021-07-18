"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from users.views import login_user
from customers.views import customer_creat_view, customer_list_view, customer_delete_view, customer_update_view

urlpatterns = [
    path('', login_user, name='login'),
    path('dasboard/', customer_list_view, name='customer_view_dasboard'),
    path('create/', customer_creat_view, name='customer_view_create'),
    path('<int:id>/delete/', customer_delete_view, name='customer_view_delete'),
    path('<int:id>/update', customer_update_view, name='customer_view_update'),
    path('admin/', admin.site.urls),
]
