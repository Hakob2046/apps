from .models import Subscribe
from django import forms

class SubscribeModelForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'