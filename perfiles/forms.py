from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import Perfil

class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=140, required=True, widget=forms.TextInput(
            attrs= {
                'placeholder':'Nombre',
                'class': 'form-control'
                } ))
    last_name  = forms.CharField(max_length=140, required=False,widget=forms.TextInput(
            attrs= {
                'placeholder':'Apellidos',
                'class': 'form-control'
                } ))
    email = forms.EmailField(required=True,widget=forms.EmailInput(
            attrs= {
                'placeholder':'Email',
                'class': 'form-control'
                } ))
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['username'].widget=forms.TextInput(
            attrs= {
                'placeholder':'Usuario',
                'class': 'form-control'
                } )

            self.fields['password1'].widget=forms.PasswordInput(
            attrs= {
                'placeholder':'Contraseña',
                'class': 'form-control'
                } )

            self.fields['password2'].widget=forms.PasswordInput(
            attrs= {
                'placeholder':'Confirma tu Contraseña',
                'class': 'form-control'
                } )


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )


    def __str__(self):
        return self.first_name



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)