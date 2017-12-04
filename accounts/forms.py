from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput
    )

    #   THE FIELDS WE WANT TO DISPLAY
    #   EMAIL and USERNAME are default USER attributes - also first_name and last_name
    #   In this case PASSWORD1 and PASSWORD2 have been customised
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'address']
        exclude = ['username']

    #   clean the passwords and ensure they are valid
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        #   to be valid the passwords must match
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    #   Override the default save method
    #   as username cannot be left empty. Set it equal to the email
    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        #   automatically set USERNAME to email address to create a unique identifier
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)