from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from organisation.models import Organisation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class BassView(TemplateView):
    template_name = 'login.html'


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('org:organisation')
                # return render(request, 'organisations.html', {'user_org': user_org})
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})


class HomeTableView(LoginRequiredMixin,TemplateView):
    template_name='table.html'