from django import forms
from .models import Url

class url_form(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']

        widgets = {
            'original_url': forms.TextInput(attrs={
                'placeholder': 'Paste Your Long URL and Short it',
            })
        }