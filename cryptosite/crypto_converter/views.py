from django.shortcuts import render
from .forms import ConvertForm
from . import currencies


def index(request):
    if request.method == 'POST':
        if 'swap_cur' in request.POST:
            amount = request.POST.get('amount')
            give = request.POST.get('give')
            take = request.POST.get('take')
            form = ConvertForm(initial={
                'amount': request.POST.get('amount'),
                'give': take,
                'take': give
            })
            price = request.POST.get('price')
        if 'get_price' in request.POST:
            form = ConvertForm(request.POST)
            amount = request.POST.get('amount')
            give = request.POST.get('give')
            take = request.POST.get('take').lower()
            give = currencies.translate_crypto(give)
            price = currencies.get_price(amount, give, take)
    else:
        price = 0
        form = ConvertForm()

    ctx = {
        'form': form,
        'price': price,
    }

    return render(request, 'crypto_converter/index.html', ctx)
