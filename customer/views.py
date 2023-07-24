from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout

from .models import Customer
# Create your views here.
def view_children(request, parent_id):
    parent_contact = Customer.objects.get(pk=parent_id)
    children = parent_contact.get_children()
    return render(request, 'customer/view_children.html', {'parent_contact': parent_contact, 'children': children})



def logout_view(request):
    logout(request)
    return redirect("base")