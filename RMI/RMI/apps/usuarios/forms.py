from django import forms
from django.contrib.auth.models import User 
from RMI.apps.usuarios.models import *
#from django.forms.widgets import PasswordInput


class Login_form(forms.Form):

	usuario = forms.CharField(label="Cedula",widget = forms.TextInput())	
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))	

class Reporte(forms.ModelForm):	

	#nombre_adjunto = forms.CharField(label='Nombre del adjunto',max_length = 50,widget = forms.TextInput())
	#adjunto_exel = forms.FileField(label='Adjunto')
	

	class Meta:
		model = Reporte_Mensual
		fields = '__all__'
		exclude = ['mes','usuario']

class UserForm(forms.ModelForm):
	first_name = forms.CharField(label="Nombres",widget=forms.TextInput())
	last_name = forms.CharField(label="Apellidos",widget=forms.TextInput())	
	password = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = User
		fields = ['email']		

class RegisterForm(forms.Form):
	first_name = forms.CharField(label="Nombres",widget=forms.TextInput())
	last_name = forms.CharField(label="Apellidos",widget=forms.TextInput())
	username = forms.CharField(label="Cedula",widget=forms.TextInput())
	email    = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))	
	
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username 
		raise forms.ValidationError('Nombre de usuario ya existe')	

	def clean_email(self):
		email = self.cleaned_data['email']
		try:		
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email 
		raise forms.ValidationError('Email ya registrado')
	
	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']			
		password_two = self.cleaned_data['password_two']

		if password_one == password_two:	
			pass 
		else:
			raise forms.ValidationError('Password no coinciden')			