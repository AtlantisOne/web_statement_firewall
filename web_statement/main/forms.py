from .models import Bid
from django.forms import ModelForm, TextInput, Textarea, HiddenInput


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['auth_user', 'num_bid', 'source_bid', 'recipient_bid', 'port_bid', 'protocol_bid',
                  'persistent_rule', 'date_rule_start', 'date_rule_end', 'justification_bid', 'description_bid']
        widgets = {
            'num_bid': TextInput(attrs={
                'placeholder': "Номер заявки"
            }),
            'source_bid': TextInput(attrs={
                'placeholder': "Источник"
            }),
            'recipient_bid': TextInput(attrs={
                'placeholder': "Получатель"
            }),
            'protocol_bid': TextInput(attrs={
                'placeholder': "Протокол"
            }),
            'port_bid': TextInput(attrs={
                'placeholder': "Порт"
            }),
            'description_bid': Textarea(attrs={
                'placeholder': "Описание"
            }),
            'justification_bid': Textarea(attrs={
                'placeholder': "Обоснование"
            })
        }

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
