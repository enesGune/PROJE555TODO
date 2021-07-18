from django.shortcuts import render

# Create your views here.

from .models import Customer
from .forms import CustomerForms


def customer_creat_view(request):

    form = CustomerForms(request.POST or None)
    if form.is_valid:
        # form.save()
        pass

    context = {
        'form': form,
    }

    return render(request, 'new_item.html', context)
