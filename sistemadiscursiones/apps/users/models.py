#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-*-encoding: utf8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
	"""docstring for UserManager"""
	
	def __create_user(self, username, email, password, is_staff,
			is_superuser, **extra_fields):
		
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, is_active=True,
			is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self.__create_user(username, email, password, False, False, 
			**extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self.__create_user(username, email, password, True, True,
			**extra_fields)
		

		

class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=50, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	avatar = models.URLField()
	status = models.BooleanField(default=False)

	objects = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username' 
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.username



class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    bio = models.TextField(null=True)

    def __unicode__(self):
        return "%s's profile" % self.user

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

# Signal while saving user
from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)