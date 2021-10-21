from django import forms
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm
from django.forms.widgets import SplitDateTimeWidget
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        exclude = ('status', 'created_at',)

        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control'}),
            'writing': forms.TextInput(attrs={'class':'form-control'}),
            'topping': CheckboxSelectMultiple,
            'decoration': CheckboxSelectMultiple,
            'berry': CheckboxSelectMultiple,
        }
