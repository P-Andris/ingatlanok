from django import forms
from django.forms import ModelForm, ValidationError
from django.utils import timezone
from .models import *

class IngatlanForm(ModelForm):
    class Meta:
        model = Ingatlan
        fields = '__all__'
        widgets = {
            'kategoria': forms.Select(attrs = {'class': 'form-control'}),
            'leiras': forms.Textarea(attrs = {'class': 'form-control'}),
            'hirdetes_datuma': forms.DateInput(format = ('%Y-%m-%d'), attrs = {
                'type': 'date',
                'class': 'form-control'
            }),
            'tehermentes': forms.CheckboxInput(attrs = {'class': 'form-check-input'}),
            'ar': forms.NumberInput(attrs = {'class': 'form-control'}),
            'kep_url': forms.TextInput(attrs = {'class': 'form-control'})
        }

    def clean_hirdetes_datuma(self):
        super().clean()

        hirdetes_datuma = self.cleaned_data.get('hirdetes_datuma', None)

        if(not hirdetes_datuma):
            hirdetes_datuma =  timezone.now().date()

        return hirdetes_datuma