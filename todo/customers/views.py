from django.shortcuts import render

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
