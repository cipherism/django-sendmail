from django.shortcuts import render
from django.urls import reverse_lazy
from emailserver.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail, EmailMessage
from  django.views.generic.edit import FormView

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Test Email Server Using Django'  
        message = str(sub['message'].value())
        recipients = str(sub['email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recipients], fail_silently=False)
        return render(request,'Appserver/success.html',{'recipients':recipients})
    return render(request,'subscribe.html',{'form':sub})

class SubscribeView(FormView):
    template_name = 'subscribe.html'
    form_class = forms.Subscribe
    success_url = reverse_lazy('Appserver:success_subs')

    def form_valid(self, form):
        subject = 'Test Email Server Using Django'
        message = form.cleaned_data['message']
        recipients = form.cleaned_data['email']
        emails = [recipients]
        
        send_email_message(subject,message,emails)
        # form.send_email()
        return super().form_valid(form)

def send_email_message(subject, message, email):
    email = EmailMessage(subject, message, to=email)
    email.send()
    
def success_subs(request):
    return render(request, 'Appserver/success.html')
        