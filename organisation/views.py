from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Organisation
from customer.models import Customer
from django.contrib.auth.models import User
from .models import OrgCustomer
# Create your views here.

class OrganisationViewSet(View):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if not request.user.is_authenticated:
            return redirect('login.html')

        user_org = Organisation.objects.filter(parent=None)
        context = {
            'user_org' : user_org
        }
        return render(request, 'organisations.html', context)

class OrganisationBranchView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        org_id = kwargs.get('id')
        if not request.user.is_authenticated:
            return redirect('login.html')
        
        parent_org = get_object_or_404(Organisation, id=org_id, created_by=user)
        child_orgs = parent_org.get_descendants(include_self=False)
        context = {
            'child_orgs':child_orgs
        }
        return render(request,'organisations_branch.html', context)


class OrganisatioDetailnViewSet(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        org_id = self.kwargs.get('id', self.kwargs.get('pk'))
        if not request.user.is_authenticated:
            return redirect('login.html')

        org = Organisation.objects.filter(id=org_id)
        org_users = User.objects.filter(customers__org_customer__organisation=org_id)
        context = {
            'org' : org,
            'org_users': org_users
        }
        return render(request, 'organisation_details.html', context)


class ListAllUserView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        if not request.user.is_authenticated:
            return redirect('login.html')
        customer_list = OrgCustomer.objects.all()
        context = {
            'customer_list' : customer_list,
        }
        return render(request, 'customer_list.html', context)