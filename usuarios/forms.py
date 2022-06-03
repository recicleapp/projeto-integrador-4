from dataclasses import field

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from .models import Coletor, Consumidor


# formulário de login customizado
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': '',
            'placeholder': ''
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': '',
            'placeholder': ''
        }
    ))



class UsuarioRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repita a senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Senhas diferentes.')
        return cd['password2']


class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ConsumidorEditForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['usuario', 'tipo']


class ColetorEditForm(forms.ModelForm):
    class Meta:
        model = Coletor
        fields = ['usuario', 'tipo']
