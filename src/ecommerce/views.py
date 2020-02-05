# from django.contrib.auth import get_user_model,authenticate,login
from django.contrib.auth import authenticate, login , get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import ContactForm,LoginForm,RegisterForm

def about(request):
	fuck = {
	"title": "hello this is title"
	}
	return render(request, "home_page.html" ,fuck)
# view for the main form which is in cconatcat page 
def contact(request): 
	contact_form = ContactForm(request.POST or None)
	fuck = {
	"form" : contact_form
	}
	
		
	return render(request, "register.html" ,fuck)


def home_page(request):
	fuck = {
	"title": "hello this is title"
	}
	# if request.user.is_authenticated():
	# 	fuck["authContent"] = "this is by authenticated"
	return render(request, "home_page.html" ,fuck)
# this  is the view for the login form
def login_page(request):
	form = LoginForm(request.POST or None)
	fuck = {
		"form": form
	}
	# for nnow to print the data i m using this
	if form.is_valid():
		print(form.cleaned_data)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			print("its workined now")
			fuck['form'] = LoginForm()
			return redirect("/login")
		else:
        # Return an 'invalid login' error message.
			print("fuck not authenticate")

	# 	username = form.cleaned_data.get("username")
	# 	password = form.cleaned_data.get("password")
	# 	user = authenticate(request, username="username", password="password")
	# 	print(user)
	# 	print(password)
	# 	if user is not None:
	# 		login(request,user)
	# 		print("fuck it works fucking shit")
	# 		fuck['form'] = LoginForm()
	# 		return redirect("/login")
	# 	else:
	# 		print("fuck not authenticate")
	return render(request, "auth/login.html",fuck)

user = get_user_model() 
# this  is the view for the register form
def register_page(request):
	form = RegisterForm(request.POST or None)
	fuck = {
		"form": form
	}
	# for now we are uding thiss to print the fucking data
	if form.is_valid():
		print(form.cleaned_data)
		# taking all the data from register form and makin a new_user with that datas
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = user.objects.create_user(username,email,password)
	return render(request, "auth/register.html", fuck)
