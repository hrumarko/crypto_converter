from django import forms

currencies = [
    ('BTC', 'BTC'),
    ('UAH', 'UAH'),
    ('ETH', 'ETH'),
    ('SOL', 'SOL'),
]


class ConvertForm(forms.Form):
    amount = forms.DecimalField(min_value=0)
    give = forms.ChoiceField(choices=currencies)
    take = forms.ChoiceField(choices=currencies)
