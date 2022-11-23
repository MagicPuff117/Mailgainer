# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mailgainer_app.models import Contact
from mailgainer_app.serializers import ContactSerializer
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from mailgainer_app.forms import ContactForm
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse

from rest_framework.filters import SearchFilter



class UserViewSet(ModelViewSet):

    queryset = Contact.objects.all()
    serializer = ContactSerializer

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'Имя': form.cleaned_data['first_name'],
                'Фамилия': form.cleaned_data['last_name'],
                'email' : form.cleaned_data['email']

            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'sergey@chernyshov117.ru', ['sergey@chernyshov117.ru'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('main:homepage')
