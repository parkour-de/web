from django import forms
from main.models import Contact


class EmailForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["email"]
