from django import forms
from . import currencies


class ConvertForm(forms.Form):
    amount = forms.DecimalField(min_value=0)
    give = forms.ChoiceField(choices=currencies.get_currencies())
    take = forms.ChoiceField(choices=currencies.get_currencies())
