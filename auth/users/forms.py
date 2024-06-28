from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

import datetime

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин или E-mail', widget=forms.TextInput(attrs={'class': 'text-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'text-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'text-input'}))

    class Meta: 
        model = get_user_model()
        fields = ['username','email','password1','password2']
        
        labels = {
            'email': 'E-mail'
        }

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
        }
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if get_user_model().objects.filter(email=email):
            raise forms.ValidationError('Такой почтовый адрес уже зарегистрирован')
        return email

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True,label='Логин', widget=forms.TextInput(attrs={'class': 'text-input'}))
    email = forms.CharField(disabled=True,label='Логин', widget=forms.TextInput(attrs={'class': 'text-input'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-5))))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'date_birth', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Старый пароль')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Новый пароль')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Повторите пароль')
