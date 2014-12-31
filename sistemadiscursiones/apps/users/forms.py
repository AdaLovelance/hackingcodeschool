#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-encoding: utf-8-*-

from django import forms
from .models import User, UserProfile
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class  ExtraDataForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username' , 'email')



class Registro(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'avatar', 'descripcion')
		widgets = {
			'username': forms.TextInput(attrs = {
				'class' : 'form-control',
				'placeholder' : 'Introduce tu nombre de usuario',
				'id' : 'username'
			}) ,

			'email' : forms.TextInput(attrs = {
				'class' : 'form-control',
				'placeholder' : 'Introduce tu email',
				'id' : 'email'
			}) ,

			'password' : forms.PasswordInput(attrs = {
				'class' : 'form-control',
				'placeholder' : 'Introduce tu password',
				'id' : 'password'
			}) ,

	
			'descripcion' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : '¿Eres sysadmin, coder, programas en varios lenguajes?.'
			     ' Describre tus habilidades ',
				'id' : 'descripcion',
				'rows' : 10
			}),

			'avatar' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Introduce una url con tu avatar',
				'id' : 'avatar',
			}),
			}
			
class Login(forms.Form):
	fields = ('username', 'password')
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'email','password', 'descripcion', 'avatar' )
    	widgets = {
		'username': forms.TextInput(attrs = {
			'class' : 'form-control',
			'placeholder' : 'Introduce tu nombre de usuario',
			'id' : 'username'
		}) ,

		'email' : forms.TextInput(attrs = {
			'class' : 'form-control',
			'placeholder' : 'Introduce tu nuevo email',
			'id' : 'email'
		}) ,

		'password' : forms.PasswordInput(attrs = {
			'class' : 'form-control',
			'placeholder' : 'Introduce tu nueva password',
			'id' : 'password'
		}) ,


		'descripcion' : forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder' : '¿Eres sysadmin, coder, programas en varios lenguajes?.'
		     ' Describre tus habilidades ',
			'id' : 'descripcion',
			'rows' : 10
		}),

		'avatar' : forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder' : 'Introduce una url con tu avatar',
			'id' : 'avatar',
		})


		}

   