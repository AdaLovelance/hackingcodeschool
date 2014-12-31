#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from  .models import User , UserProfile


class UserAdmin(UserAdmin):

	fieldsets = (
		('User', {'fields': ('username', 'password')}),
		
		('Persona Info', {'fields' : ('first_name',
									   'last_name',
									  
									    'email',
									    'avatar')}),
		
		('Permissions' , {'fields' : ('is_active',
			                          'is_staff',
			                          'is_superuser',
			                          'groups',
			                          'user_permissions')}),
		
		
		
	
		)
		


admin.site.register(User, UserAdmin)

