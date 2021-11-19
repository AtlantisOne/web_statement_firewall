from django.shortcuts import render
from .models import Bid, Signers_bid
from .forms import BidForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from docxtpl import DocxTemplate
from django.shortcuts import get_object_or_404
import datetime
import jinja2


# def about(request):
#     return render(request, 'main/about.html')


# @login_required
# def create_django(request):
#     error_bid = ''
#     complete_bid = ''
#     if request.method == 'POST':
#         form = BidForm(request.POST)
#         if form.is_valid():
#             form.save()
#             complete_bid = 'Заявка успешно добавлена'
#         else:
#             error_bid = 'Форма была заполнена неверно'
#     form = BidForm()
#     data = {
#         'form': form,
#         'error': error_bid,
#         'complete_bid': complete_bid,
#         # 'current_user': curr_user(request)
#     }
#     return render(request, 'main/create_django.html', data)


def gen_num_bid():
    pass


def gen_docfile(request, data, signers=None):
    doc = DocxTemplate("main/docs/bid.docx")
    filepath = r'main/docs/' + data.num_bid + '.docx'

    context = {'num_bid': data.num_bid,
               'source_bid': data.source_bid,
               'recipient_bid': data.recipient_bid,
               'port_bid': data.port_bid,
               'protocol_bid': data.protocol_bid,
               'description_bid': data.description_bid,
               'justification_bid': data.justification_bid,
               'persistent_rule': data.get_persistent_rule(),
               'description_bid ': data.description_bid,
               'date_rule_start': data.get_date_rule_start(),
               'date_rule_end': data.get_date_rule_end(),
               'auth_user': request.user.get_full_name(),
               'email_user': request.user.email,
               'user_phone_bid': data.user_phone_bid,
               'user_department_name_bid': data.user_department_name_bid,
               'boss_department_name_bid': data.boss_department_name_bid,
               'boss_full_name_bid': data.boss_full_name_bid,
               'signers': signers,
               'curr_date': datetime.datetime.strftime(datetime.datetime.now(), '« %d »   %m   %Yг.')
               }
    doc.render(context)
    doc.save(filepath)


@login_required
def create_html(request, form=None):
    error_bid = ''
    complete_bid = ''
    num_bid = ''

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.num_bid = "OP-" + str(instance.id)
            num_bid = instance.num_bid
            signers = Signers_bid.objects.all()
            gen_docfile(request, instance, signers)
            instance.save()
            complete_bid = f'Заявка успешно добавлена: {num_bid}'
        else:
            error_bid = 'Форма была заполнена неверно'

    form = BidForm()
    data = {
        'form': form,
        'error_bid': error_bid,
        'complete_bid': complete_bid,
        'num_bid': num_bid,
    }
    return render(request, 'main/create_html.html', data)


@login_required
def bid_clone(request, id):
    error_bid = ''
    complete_bid = ''
    num_bid = ''
    instance = get_object_or_404(Bid, id=id)

    if request.method == 'POST':
        form = BidForm(request.POST or None)
        if form.is_valid():
            instance = form.save()
            instance.num_bid = "OP-" + str(instance.id)
            num_bid = instance.num_bid
            signers = Signers_bid.objects.all()
            gen_docfile(request, instance, signers)
            instance.save()
            complete_bid = f'Заявка успешно добавлена: {num_bid}'
        else:
            error_bid = 'Форма была заполнена неверно'

    form = BidForm()
    data = {
        'form': form,
        'error_bid': error_bid,
        'complete_bid': complete_bid,
        'num_bid': num_bid,
        'inputs': {'num_bid': instance.num_bid,
                   'source_bid': instance.source_bid,
                   'recipient_bid': instance.recipient_bid,
                   'port_bid': instance.port_bid,
                   'protocol_bid': instance.protocol_bid,
                   'description_bid': instance.description_bid,
                   'justification_bid': instance.justification_bid,
                   'persistent_rule': instance.persistent_rule,
                   'description_bid': instance.description_bid,
                   'date_rule_start': instance.date_rule_start,
                   'date_rule_end': instance.date_rule_end,
                   'auth_user': request.user.get_full_name(),
                   'email_user': request.user.email,
                   'user_phone_bid': instance.user_phone_bid,
                   'user_department_name_bid': instance.user_department_name_bid,
                   'boss_department_name_bid': instance.boss_department_name_bid,
                   'boss_full_name_bid': instance.boss_full_name_bid
                   }
    }
    return render(request, 'main/bid_clone.html', data)


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
    template_name = 'main/bid_edit.html'
    context_object_name = 'bid_edit'
    fields = ['num_bid', 'auth_user', 'source_bid', 'recipient_bid', 'port_bid', 'protocol_bid',
              'persistent_rule', 'date_rule_start', 'date_rule_end', 'description_bid', 'justification_bid',
              'user_phone_bid', 'user_department_name_bid', 'boss_department_name_bid',
              'boss_full_name_bid']


class Bid_delete(DeleteView):
    model = Bid
    success_url = '/'
    context_object_name = 'bid_delete'
    template_name = 'main/bid_delete.html'

# def index(request):
#     bids = Bid.objects.order_by('-created_date_bid')
#     return render(request, 'main/index.html', {'bids': bids})


# def curr_user(request):
#     current_user = request.user.id
#     return current_user

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
