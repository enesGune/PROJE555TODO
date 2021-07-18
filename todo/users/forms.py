from django import forms
from .models import LoginUser


class LoginForms(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Kullanıcı Adı'}))
    password = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Şifre'}))

    class Meta:
        model = LoginUser
        fields = [
            'username',
            'password',
        ]
