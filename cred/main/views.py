from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from adminapp.models import member

def register(request):

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if password1 == password2:
			if User.objects.filter(username = username).exists():
				messages.info(request,'Username already exists')
				return redirect('register')
			elif User.objects.filter(email = email).exists():
				messages.info(request,'Email already exists')
				return redirect('register')
			else:
				user = User.objects.create_user(
					first_name = first_name,
					username = username, 
					email = email,
					password = password1
				)
				user.save();
				print('User registered.')
				return redirect('user_login')
		else:
			messages.error(request,'password didn\'t match.')
			return redirect('register')
	else:
		return render(request, 'register.html')


def user_login(request):
	if 'username' in request.session:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		# if username == 'son' and password == '1234':
		# 	return JsonResponse(
		# 		{'success': True},
		# 		safe = False

		# 	)
		# else:

		# 	return JsonResponse(
		# 		{'success': True},
		# 		safe = False
		# 	)
		user = authenticate(username = username, password = password)

		if user is not None:
			request.session['username'] = username
			return redirect('home')
		else:
			messages.info(request, 'Invalid username or password')
			return redirect('user_login')
	return render(request, 'login.html')

def user_logout(request):
	if 'username' in request.session:
		request.session.flush()
	return redirect('user_login')

def home(request):
	if 'username' in request.session:
		return render(request, 'home.html')
	return redirect('user_login')

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
