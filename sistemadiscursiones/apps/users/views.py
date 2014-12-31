#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.views.generic import View, DetailView, CreateView, ListView, UpdateView
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model

from .forms import ExtraDataForm, Registro, Login, UserProfileForm
from .models import User, UserProfile
from apps.discuss.models import Question



class ExtraDataView(View):
	
	def  get(self, request, *args, **kwargs):
		if request.user.status:
			return redirect('/')
		else:
			return render(request, 'users/extra_data.html')

	def post(self, request, *args, **kwargs):
		form = ExtraDataForm(request.POST)
		if form.is_valid():
			request.user.username = request.POST['username']
			request.user.email = request.POST['email']
			request.user.status = True
			request.user.save()
			send_email(request)
			return redirect('/')
		else:
			error_username = form['username'].errors.as_text()
			error_email = form['email'].errors.as_text()
			ctx = {'error_username':error_username, 'error_email':error_email}
			return render(request, 'users/extra_data.html', ctx)



def  LogOut(request):
	logout(request)
	return redirect('/')


def send_email(request):

	msg = EmailMessage( subject = 'Bienveni@',
						from_email = 'Hacking Code School' '<ada_lovelance@hackincodeschool.net>',
						to = [request.user.email])
	msg.template_name = 'welcome'
	msg.template_content = {

		'std_contend00' : '<h1>Hola %s Bienvenid@ a Hacking Code School</h1>' % request.user
	}
	msg.send()




class UserDetailView(DetailView):

	model = User
	context_object_name = 'user'
	slug_field = 'username'

	def get_context_data(self, **kwargs):
		context = super(UserDetailView, self).get_context_data(**kwargs)
		questions = Question.objects.filter(user = context['object']).order_by('created')
		tags = [ question.tag.all() for question in questions]
		context['quest_tags'] = zip(questions, tags)

		facebook = context['object'].social_auth.filter(provider='facebook')
		if facebook:
			context['facebook'] = facebook[0].extra_data['id']

		twitter = context['object'].social_auth.filter(provider='twitter')
		if twitter:
			context['twitter'] = twitter[0].extra_data['access_token']['screen_name']

		google = context['object'].social_auth.filter(provider='google')
		if google:
			context['google'] = google[0].extra_data['id']

		return context

"""
	def form_valid(self, form):
		super(RegistrView, self).form_valid(form)
		form.save()

	def post(self, request, *args, **kwargs):
		form = Registro(request.POST)	

		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			logueo(form.cleaned_data['username'], form.cleaned_data['password'], request )
			return redirect('/')
		else:
			error_username = form['username'].errors.as_text()
			error_email = form['email'].errors.as_text()
			ctx = {'error_username':error_username, 'error_email':error_email, }
			return render(request, 'users/registro.html' and ctx)
"""
def login_Registro(request):

	formRegistro = Registro(request.POST or None)
	formLogin = Login(request.POST or None)
	if formRegistro.is_valid():
		user = formRegistro.save()
		user.set_password(user.password)
		user.save()
		logueo(formRegistro.cleaned_data['username'], formRegistro.cleaned_data['password'], request )
		return redirect('/')
	if formLogin.is_valid():
		logueo(formLogin.cleaned_data['username'], formLogin.cleaned_data['password'], request )
		return redirect('/')
	return render(request, 'users/registro.html', {'formRegistro': formRegistro, 'formLogin':formLogin})


def login_User(request):
	form = Login(request.POST or None)
	if form.is_valid():
		usuario = authenticate(username = request.POST["username"], password = request.POST["password"])
		if usuario is not None:
			if usuario.is_active:
				login(request, usuario)
				return redirect('/')
	return render(request, 'users/registro.html', {'form': form})
	


def logueo(username,password, request):
	
	usuario = authenticate(username = username, password = password)
	if usuario is not None:
		if usuario.is_active:
			login(request, usuario)


 
class UserProfileEditView(UpdateView):
    form_class = UserProfileForm
    template_name = "users/perfil.html"
    model = User
    success_url = "/"
   
    def get_object(self,  queryset=None, **kwargs):
    	return User.objects.get_or_create(username=self.request.user)[0]


