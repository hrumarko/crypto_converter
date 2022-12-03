from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConvertForm


def index(request):
    form = ConvertForm()
    ctx = {
        'form': form,
    }

    return render(request, 'crypto_converter/index.html', ctx)
