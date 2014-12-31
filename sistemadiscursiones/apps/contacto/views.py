from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ContactoView(TemplateView):
	template_name = 'contacto/contacto.html'