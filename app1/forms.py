from django import forms
from .models import Hotels

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = '__all__'

