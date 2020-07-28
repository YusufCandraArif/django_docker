from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from .forms import SignUpForm

from django.urls import reverse_lazy

class HomeView(TemplateView):
    #url/html ini ada di templates/common
    template_name = 'common/home.html'

class SignUpView(CreateView):
    # dengan mixin, CreateView akan membuat view signup
    form_class = SignUpForm

    #"home" didapat dari urls, nama url 
    success_url = reverse_lazy("home")

    #url/html ini ada di templates/common
    template_name = 'common/register.html'

class DashboardView(TemplateView):
    #url/html ini ada di templates/common
    template_name = 'common/dashboard.html'
