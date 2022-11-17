from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField


class SignUpForm(UserCreationForm):

    username = CharField(
        widget=TextInput(
            attrs={
                'name': 'name',
                'id': 'name',
                'placeholder': 'Your Username',
                'class': 'form-control form-control-lg'
            }
        )
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'pass',
                'id': 'pass',
                'placeholder': 'Enter Your Password',
                'class': 'form-control form-control-lg'
            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 're_pass',
                'id': 're_pass',
                'placeholder': 'Repeat Your Password',
                'class': 'form-control form-control-lg'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'name': 'email',
                'id': 'email',
                'placeholder': 'Enter Your Email',
                'class': 'form-control form-control-lg'
            }
        )
    )


class SignInForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={
                'name': 'your_name',
                'id': 'your_name',
                'placeholder': 'Enter Your Username',
                'class': 'form-control form-control-lg'
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'your_pass',
                'id': 'your_pass',
                'placeholder': 'Enter Your Password',
                'class': 'form-control form-control-lg'
            }
        )
    )
