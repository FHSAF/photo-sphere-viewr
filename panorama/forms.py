from django import forms
from django.forms import widgets
from .models import Room, ComponentImage

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('title', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',   'placeholder': 'Enter the title'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = ComponentImage
        exclude = ('room',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',   'placeholder': 'Enter the title'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control',   'placeholder': 'Enter the Longitude'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control',   'placeholder': 'Enter the Latitude'}),
        }