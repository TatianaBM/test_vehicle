from django.contrib.auth.forms import forms, User, UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'User Name',
            'email': 'Email',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
        }
