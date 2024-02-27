from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def envia_email(request):
    send_mail('Assunto', 'Email')
    return HttpResponse('ola')
