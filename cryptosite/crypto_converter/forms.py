from django import forms
from . import currencies


class ConvertForm(forms.Form):
    amount = forms.DecimalField(
        label='',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'amount',
            'placeholder': 'Input your amount',
        })
    )
    give = forms.ChoiceField(
        choices=currencies.get_currencies(),
        widget=forms.Select(attrs={
            'class': 'give-ch'
        })
    )
    take = forms.ChoiceField(
        choices=currencies.get_currencies(),
        widget=forms.Select(attrs={
            'class': 'take-ch'
        })
    )
