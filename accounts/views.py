from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import  SuccessMessageMixin

from .forms import SignUpForm


class SignUp(CreateView, SuccessMessageMixin):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    success_message = "Account was succesfully created"
