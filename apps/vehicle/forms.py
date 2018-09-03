from django import forms
from apps.vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle

        fields = [
            'enrollment',
            'owner',
            'type',
            'brand',
            'model',
            'color',
            'photo',
            'description',
        ]
        labels = {
            'enrollment': 'Enrollment',
            'owner': 'Owner',
            'type': 'Type',
            'brand': 'Brand',
            'model': 'Model',
            'color': 'Color',
            'photo': 'Photo',
            'description': 'Description',
        }
        widgets = {
            'enrollment': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control file_image'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
