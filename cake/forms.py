from django import forms
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm

from django.contrib.admin.widgets import AdminSplitDateTime

from .models import Order


class OrderForm(ModelForm):
    delivery_at = forms.SplitDateTimeField(
        widget=AdminSplitDateTime,
        label='Дата и время доставки',
    )

    class Meta:
        model = Order
        fields = ('__all__')
        exclude = ('status', 'created_at', 'customer')

        widgets = {
            'layer': forms.Select(attrs={'class': 'form-control'}),
            'form': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control'}),
            'writing': forms.TextInput(attrs={'class':'form-control'}),
            'topping': CheckboxSelectMultiple,
            'decoration': CheckboxSelectMultiple,
            'berry': CheckboxSelectMultiple,
        }
