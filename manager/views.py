from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

def isadmin(function):
	def wrapper(request):
		if request.user.is_superuser:
			return function(request)
		else:
			raise PermissionDenied
	return wrapper

def main(request):
	return HttpResponse('Vista general')

@login_required
def userview(request):
	return HttpResponse('Only users and Admin')

@login_required
@isadmin
def adminview(request):
	return HttpResponse('Only admins')

def denied(request):
	raise PermissionDenied