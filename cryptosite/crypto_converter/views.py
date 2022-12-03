from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    form = ''
    ctx = {
        'form': form
    }

    return render(
        request, 'crypto_converter/index.html', ctx
    )
