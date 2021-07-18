from django import forms
from .models import LoginPage


class LoginForms(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Kullanıcı Adı'}))
    password = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Şifre'}))

    class Meta:
        model = LoginPage
        fields = [
            'username',
            'password',
        ]
