from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from main.models import Manager


class ProfilePageForm(forms.ModelForm):
    """
    User profile form.
    """
    class Meta:
        model = Manager
        fields = ('bio', 'profile_pic')
        
        widgets = {
            'bio': forms.Textarea(attrs={'class': "form-control",
                'placeholder': "характеристика ..."}),
        }


class EditProfileForm(UserChangeForm):
    """
    User profile edit form.
    """
    email = forms.EmailField(label='Email', 
        widget=forms.EmailInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label='Имя', max_length=100, 
        widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Фамилия', max_length=100, 
        widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class PasswordChangingForm(PasswordChangeForm):
    """
    User password change form.
    """
    old_password = forms.CharField(label='Старый пароль', 
        widget=forms.PasswordInput(attrs={'class': "form-control", 'type':'password'}))
    new_password1 = forms.CharField(label='Новый пароль', 
        widget=forms.PasswordInput(attrs={'class': "form-control", 'type':'password'}))
    new_password2 = forms.CharField(label='Подтверждение нового пароля', 
        widget=forms.PasswordInput(attrs={'class': "form-control", 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
