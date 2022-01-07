from .models import Bid, Rule, SourceBid, RecipientBid
from django.forms import ModelForm, TextInput, Textarea, HiddenInput, modelformset_factory, formset_factory
from django import forms


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['num_bid', 'status_bid', 'auth_user', 'persistent_rule', 'date_rule_start', 'date_rule_end',
                  'justification_bid', 'description_bid',
                  'user_phone_bid', 'user_department_name_bid', 'boss_department_name_bid', 'boss_full_name_bid']

        # def __init__(self, *args, **kwargs):
        #     super(BidForm, self).__init__(*args, **kwargs)
        #     for field_name, field in self.fields.items():
        #         field.widget.attrs['class'] = 'form-control'
        #         field.widget.attrs['placeholder'] = 'field_name'
        #         field.widget.attrs['value'] = 'request.user.id'
        # widgets = {
        #     'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),
        #     'status_bid': TextInput(attrs={
        #         'placeholder': "Статус заявки"
        #     }),
        #     'auth_user': TextInput(attrs={
        #         'placeholder': "Авторизованный пользователь"
        #     }),
        #     'persistent_rule': TextInput(attrs={
        #         'placeholder': "Постоянное правило"
        #     }),
        #     'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),
        #     'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),
        #     'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),            'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),
        #     'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),
        #     'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),
        #     'num_bid': TextInput(attrs={
        #         'placeholder': "Номер заявки"
        #     }),
        #
        #     'description_bid': Textarea(attrs={
        #         'placeholder': "Описание"
        #     }),
        #     'justification_bid': Textarea(attrs={
        #         'placeholder': "Обоснование"
        #     })
        # }


RuleFormset = modelformset_factory(
    Rule,
    fields=('bid', 'port_bid', 'protocol_bid'),
    extra=1,
    widgets={
        'port_bid': TextInput(attrs={'placeholder': "Порт",})
    }
)

SourceBidFormset = modelformset_factory(
    SourceBid,
    fields=('bid', 'source_bid'),
    extra=1,
    widgets={
        'source_bid': TextInput(attrs={'placeholder': "Источник",})
    }
)

RecipientBidFormset = modelformset_factory(
    RecipientBid,
    fields=('bid', 'recipient_bid'),
    extra=1,
    widgets={
        'recipient_bid': TextInput(attrs={'placeholder': "Получатель",})
    }
)


# class RuleForm(ModelForm):
#     class Meta:
#         model = Rule
#         fields = ['bid', 'source_bid', 'recipient_bid', 'port_bid', 'protocol_bid', ]
#         widgets = {
#             'bid': TextInput(attrs={
#                 'placeholder': "Номер заявки"
#             }),
#             'source_bid': TextInput(attrs={
#                 'placeholder': "Источник"
#             }),
#             'recipient_bid': TextInput(attrs={
#                 'placeholder': "Получатель"
#             }),
#             'protocol_bid': TextInput(attrs={
#                 'placeholder': "Протокол"
#             }),
#             'port_bid': TextInput(attrs={
#                 'placeholder': "Порт"
#             }),
#         }

# from django import forms
# from django.contrib.auth.models import User

# class LoginForm(ModelForm):
#
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'],label = 'Логин'
#         self.fields['password'],label = 'Пароль'

#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filter(username=username).exists():
#             raise forms.ValidationError(f'Пользователь с логином {username} не найден')
#         user = User.objects.filter(username=username).first()
#         if user:
#             if not user.check_password(password):
#                 raise forms.ValidationError('Неверный пароль')
#         return self.cleaned_data
#
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
