from django import forms
from apps.owner.models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            'document',
            'first_name',
            'last_name',
            'address',
            'cellphone',
            'email',
            'photo',
            'age',
        ]
        labels = {
            'document': 'Document',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'address': 'Address',
            'cellphone': 'Cellphone',
            'email': 'Email',
            'photo': 'Photo',
            'age': 'Age',
        }
        widgets = {
            'document': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'required': "required"}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
            'photo': forms.FileInput(attrs={'class': 'form-control file_image'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'required': "required"}),
        }
