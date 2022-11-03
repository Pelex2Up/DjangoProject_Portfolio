from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomLoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    remember_me = forms.BooleanField(required=False)
