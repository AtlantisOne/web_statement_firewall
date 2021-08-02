from django.shortcuts import render
from django.http import HttpResponse
from .models import Bid
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
