from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from ideas.models import Idea

def register(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['password-confirm']:
			try:
				user = User.objects.get(username=request.POST['username'])
				messages.add_message(request, messages.ERROR, 'User already exists! please use another name')
				return redirect('accounts:register')
 				#return redirect('accounts:register')
			except User.DoesNotExist:
				user = User.objects.create_user(username = request.POST['username'],password = request.POST['password'])
				messages.add_message(request, messages.SUCCESS, 'Successful')
				return redirect('accounts:login')
		else:
			messages.add_message(request, messages.ERROR, 'Passwords DO NOT MAtch')
			return redirect('accounts:register')
	else:
		return render(request, 'accounts/register.html', {'page_title':'Register'})

 				#return redirect('accounts:register')
				#Else register use
		#else:
 			# return render(request, messages.ERROR, 'Passwords DO NOT MAtch')
 			#return redirect('accounts:register')
 	# else:
 	# 	 return render(request, 'accounts/register.html', {'page_title':'Register'})

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(request, username = request.POST['username'],password = request.POST['password'])
		if user is not None:
			auth.login(request,user)
			messages.add_message(request, messages.SUCCESS, 'Successful')
			return redirect('welcome:home')

		else:
			messages.add_message(request, messages.ERROR, 'username and Passwords DO NOT MAtch')
			return redirect('accounts:login')
	else:
 		return render(request, 'accounts/login.html', {'page_title':'Login'})

def logout(request):
	auth.logout(request)
	messages.add_message(request, messages.SUCCESS, 'Successfully logged_out')
	return redirect('accounts:login')

@login_required(login_url="accounts:login")
def dashboard(request):
	user = request.user
	data = Idea.objects.filter(user=user)
	print(data)
	return render(request, 'accounts/dashboard.html', {'page_title':'Dashboard', 'ideas':data})


 	