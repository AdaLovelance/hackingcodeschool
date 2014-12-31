from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class BibliotecaView(TemplateView):
	template_name = 'biblioteca/biblioteca.html'