from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data('username')
        qs = User.objects.filter(username_iexact=username)

        if not qs.exists():
            raise forms.ValidationError('Username hatalı!!')

        return username
