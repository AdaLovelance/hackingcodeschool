#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from apps.users.models import User
from django.contrib import admin


class Calsession(models.Model):
    titulo = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    cuerpo = models.TextField(max_length=10000, blank=True)
    creada = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField(blank=True)
    creador = models.ForeignKey(User, blank=True, null=True)
    recordatorio = models.BooleanField(default=False)

    def __unicode__(self):
        if self.titulo:
            return unicode(self.creador) + u" - " + self.titulo
        else:
            return unicode(self.creador) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return "<i>%s</i> - %s" % (self.titulo, self.snippet)
        else:
            return self.titulo
    short.allow_tags = True

    
### Admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ["creada", "fecha", "titulo", "snippet"]
    list_filter = ["creador"]

admin.site.register(Calsession, EntryAdmin)
# Create your models here.
