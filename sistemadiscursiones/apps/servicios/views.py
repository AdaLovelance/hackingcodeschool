from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ServiciosView(TemplateView):
	template_name = 'servicios/servicios.html'