#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-*- encoding: utf-8 -*-

from django import forms
from .models import Question


class CreateQuestionForm(forms.ModelForm):

	title = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Escribe aquí el enunciado de tu pregunta'

		}))

	description = forms.CharField(widget = forms.Textarea(attrs={
				'class' : 'form-control',
				'placeholder' : 'Desarrolla aquí tu pregunta',
				'rows' : 6
	}))

	etiqueta = forms.CharField(widget = forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Escribe la etiqueta de tu pregunta',
				
	}))

	class Meta:
		model = Question





	