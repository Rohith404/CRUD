from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from adminapp.models import member
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def admin1(request):
	if request.session.has_key('password'):
		return redirect('owner')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			if username == 'use' and password == 'pass':
				request.session['password']=password
				return JsonResponse(
					{'success':True},
				  	safe = False
				)
			else:
				return JsonResponse(
					{'success':False},
				  	safe = False
				)
		else:
			return render(request, 'admin1.html')

def owner(request):
	if request.session.has_key('password'):
		mem = member.objects.all()

		context = {
			'mem':mem,
		}
		return render(request, 'owner.html',context)

	return redirect('admin1')

def add(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		password = request.POST.get('password')

		mem = member(
			first_name = first_name, 
			username = username, 
			email = email,
			phone = phone,
			password = password,
		)
		mem.save()
		return redirect('owner')

	return render(request, 'owner.html')

def edit(request):

	mem = member.objects.all()
	context = {
		'mem': mem,
	}

	return redirect(request, 'owner.html')

def update(request,id):

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		password = request.POST.get('password')

		mem = member(
			id = id,
			first_name = first_name,
			username = username,
			email = email,
			phone = phone,
			password = password,
		)
		mem.save()
		return redirect('owner')

	return redirect(request, 'owner.html')

def delete(request,id):

	mem = member.objects.filter(id = id)
	mem.delete()

	context = {
		'mem':mem,
	}

	return redirect('owner')

def admin_logout(request):
	if request.session.has_key('password'):
		request.session.flush()
	return redirect('admin1')
