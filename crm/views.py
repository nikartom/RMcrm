from django.shortcuts import  render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def homepage(request):
    	return render(request=request, template_name='crm/home.html')

def register_request(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Регистрация прошла успешно!" )
			return redirect("main:homepage")
		messages.error(request, "Регистрация не удалась. Проверьти правильность заполнения формы")
	form = UserRegistrationForm()
	return render (request=request, template_name="crm/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Вы вошли как {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Неверное имя пользователя или пароль!")
		else:
			messages.error(request,"Неверное имя пользователя или пароль!")
	form = AuthenticationForm()
	return render(request=request, template_name="crm/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Вы успешно вышли") 
	return redirect("main:homepage")