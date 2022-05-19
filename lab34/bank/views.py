from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from . import models
from .models import Manager, User, Bank, BankApplication
from django.views.generic import CreateView, ListView

from django.contrib import messages

# Create your views here.
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import LoginForm
from .models import Client

class StartPageView(View):
    template_name = 'bank/start_page.html'

    def get(self, request):
        return render(request, self.template_name)


class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'bank/signup.html'

    def form_valid(self, form):
        current_user = form.save()
        get_user=User.objects.filter(pk=current_user.id).first()
        client=Client()
        client.user=get_user
        client.save()
        return super().form_valid(form)



class LoginView(View):
    template_name = 'bank/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            user=User.objects.get(username=form.cleaned_data['username'])
            if user is not None:
                login(request, user)
                client_exists = Client.objects.filter(user=user).exists()
                if client_exists:
                    return render(request,'bank/client/client_base.html',context={'client':user})
                manager_exists = Manager.objects.filter(user=user).exists()
                if manager_exists:
                    return render(request,'bank/manager/manager_base.html',context={'manager':user})
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class ClientPageView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'bank/client/client_base.html'

    def get(self, request):
        first_name=User.first_name

        return render(request, self.template_name, context={'client':request.user})


class ClientBanksView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Bank
    template_name = 'bank/client/client_banks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_client = Client.objects.get(user=self.request.user)
        client_banks = current_client.banks
        all_banks=Bank.objects.all()
        context['client_banks'] = client_banks
        context['all_banks'] = all_banks
        return context


class SendApplicationView(LoginRequiredMixin,ListView):
    login_url = 'login'
    template_name = 'bank/client/confirm_application.html'
    context_object_name = 'bank_name'

    def get_queryset(self):
        current_client = Client.objects.get(user=self.request.user)
        bank = Bank.objects.get(pk=self.kwargs['pk'])
        for application in BankApplication.objects.all():
            if application.bank_id == self.kwargs['pk'] and application.client_id == current_client.id:
                return bank.name
        BankApplication.objects.create(bank_id=self.kwargs['pk'], client_id=current_client.id)

        return bank.name


class ManagerPageView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'bank/manager/manager_base.html'

    def get(self, request):

        return render(request, self.template_name, context={'manager': request.user})


class ApplicationsView(LoginRequiredMixin,ListView):
    login_url = 'login'
    template_name = 'bank/manager/manager_applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        current_manager = Manager.objects.get(user=self.request.user)
        bank = Bank.objects.get(pk=current_manager.bank.id)
        bank_applications = BankApplication.objects.filter(bank_id=bank.id)
        clients_applications=[]
        for application in bank_applications:
            client = Client.objects.get(pk=application.client_id)
            clients_applications.append(client.user)
        return clients_applications







