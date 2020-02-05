from django import forms
from django.contrib.auth import authenticate, login , get_user_model
# from django import signUp
user = get_user_model()
# thisis is for the main contact page form class
class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","Placeholder": "Your Email"}))
	content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Only gamil adress allow")
		return email
# class for login 
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
# class for register
class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
	# for username exists to cto show msg
	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = user.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username
	# to email is taken please use another username
	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = user.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email
	# for both password shoud match both pasword fields in passcode shud matxch
	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Password didn't match")
		return data
