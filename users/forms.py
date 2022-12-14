from django import forms
from users.models import UserModel
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ['username', 'Ismingiz', 'Sharifingiz', 'Qayerdansiz', 'phone', 'password', 'confirm_password']

        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):

        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parollar har xil...')

        return self.cleaned_data['confirm_password']
