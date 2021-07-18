from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import Customer
from .forms import CustomerForms


def customer_creat_view(request):

    form = CustomerForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForms()
    context = {
        'form': form,
    }

    return render(request, 'new_item.html', context)


def customer_list_view(request):
    queryset = Customer.objects.all()
    context = {
        'list': queryset,
    }
    return render(request, 'dasboard.html', context)


def customer_delete_view(request, id):
    obj = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object": obj
    }
    return render(request, "delete.html", context)


def customer_update_view(request, id=id):
    obj = get_object_or_404(Customer, id=id)
    form = CustomerForms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "new_item.html", context)
