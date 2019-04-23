from django import forms
from .models import ContactUs, About


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('',)


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = '__all__'
