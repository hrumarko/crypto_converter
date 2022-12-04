from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConvertForm
from . import currencies


def index(request):
    if request.method == 'POST':
        form = ConvertForm(request.POST)
        amount = request.POST.get('amount')
        give = request.POST.get('give')
        take = request.POST.get('take').lower()
        give = currencies.translate_crypto(give)
        print(f'give = {give}, take = {take}')
        price = currencies.get_price(amount, give, take)
        
    else:
        amount = 0
        form = ConvertForm()

    ctx = {
        'form': form,
        'price': price,
    }

    return render(request, 'crypto_converter/index.html', ctx)
