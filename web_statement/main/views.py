from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bid
from .forms import BidForm
import time
# Create your views here.

# def index(request):
#     data = {
#         'title': 'Главная страниw',
#         'values': ['some', 'hello'],
#         'obj': {
#             'car1': 'bmw1',
#             'car2': 'bmw2',
#             'car3': 'bmw3',
#         }
#
#     }
#     return render(request, 'main/index.html', data)

def index(request):
    bids = Bid.objects.order_by('-created_date_bid')
    return render(request, 'main/index.html', {'bids': bids})

def about(request):
    return render(request, 'main/about.html')

def test(request):
    return render(request, 'main/test.html')

def create_jango(request):
    error_bid = ''
    complete_bid = ''
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
            complete_bid = 'Заявка успешно добавлена'
            # time.sleep(3)
            # return redirect('home')
        else:
            error_bid = 'Форма была заполнена неверно'

    form = BidForm()
    data = {
        'form': form,
        'error': error_bid,
        'complete_bid': complete_bid
    }
    return render(request, 'main/create_jango.html', data)

def create_html(request):

    form = BidForm()
    data = {
        'form': form
    }

    return render(request, 'main/create_html.html', data)
