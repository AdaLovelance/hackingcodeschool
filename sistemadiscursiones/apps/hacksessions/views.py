#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HacksessionsView(TemplateView):
	template_name = 'hacksessions/hacksessions.html'

class HackprivView(TemplateView):
	template_name = 'hacksessions/hackpriv.html'

class HackpubView(TemplateView):
	template_name = 'hacksessions/hackpub.html'

class ProxHackView(TemplateView):
	template_name = 'hacksessions/proxhack.html'



import time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

from .models import *

mnames = "Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre"
mnames = mnames.split()


@login_required
def calendario(request, year=None):
    """Main listing, years and months; three years per page."""
    # prev / next years
    if year: year = int(year)
    else:    year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # create a list of months for each year, indicating ones that contain entries and current
    for y in [year, year+1, year+2]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False   # are there entry(s) for this month; current month?
            entries = Calsession.objects.filter(fecha__year=y, fecha__month=n+1)

            if entries:
                entry = True
            if y == nowy and n+1 == nowm:
                current = True
            mlst.append(dict(n=n+1, name=month, entry=entry, current=current))
        lst.append((y, mlst))

    return render_to_response("hacksessions/proxhack.html", dict(years=lst, user=request.user, year=year))