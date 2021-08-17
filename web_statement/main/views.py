from django.shortcuts import render
from .models import Bid
from .forms import BidForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


def index(request):
    bids = Bid.objects.order_by('-created_date_bid')
    return render(request, 'main/index.html', {'bids': bids})


def about(request):
    return render(request, 'main/about.html')


def test(request):
    return render(request, 'main/test.html')


@login_required
def create_jango(request):
    error_bid = ''
    complete_bid = ''
    current_user = request.user.id
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
            complete_bid = 'Заявка успешно добавлена'
        else:
            error_bid = 'Форма была заполнена неверно'
    form = BidForm()
    data = {
        'form': form,
        'error': error_bid,
        'complete_bid': complete_bid,
        'current_user': current_user
    }
    return render(request, 'main/create_jango.html', data)


@login_required
def create_html(request):
    error_bid = ''
    complete_bid = ''
    current_user = request.user.id
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
            complete_bid = 'Заявка успешно добавлена'
        else:
            error_bid = 'Форма была заполнена неверно'

    form = BidForm()
    data = {
        'form': form,
        'error': error_bid,
        'complete_bid': complete_bid,
        'current_user': current_user
    }
    return render(request, 'main/create_html.html', data)


@login_required
def user_bids(request):
    if request.user.is_staff:
        context = {
            'posts': Bid.objects.order_by('-created_date_bid')
        }
    else:
        context = {
            'posts': Bid.objects.filter(auth_user=request.user).order_by('-created_date_bid')
        }
    return render(request, 'main/index.html', context)


class Bid_detail(DetailView):
    model = Bid
    template_name = 'main/bid_detail.html'
    context_object_name = 'bid_detail'

class Bid_edit(UpdateView):
    model = Bid
    template_name = 'main/create_jango.html'
    # fields = ['num_bid']
    form_class = BidForm

class Bid_delete(DeleteView):
    model = Bid
    success_url = '/'
    context_object_name = 'bid_delete'
    template_name = 'main/bid_delete.html'
# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         form = LoginForm(request.POST or None)
#         # categories = Category.objects.all()
#         context = {'form': form}
#         # context = {'form': form, 'categories': categories}
#         return render(request, 'login.html', context)

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'main/create_html.html', {'form': form})

# def auth_user_id(request):
#     auth_user_id = request.user.id
#     form = BidForm(request.POST)
#     id = {
#         'form': form,
#         'auth_user_id': auth_user_id
#     }
#     return render(request, 'main/create_html.html', id)


# import time
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
