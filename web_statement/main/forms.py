from .models import Bid
from django.forms import ModelForm, TextInput, Textarea

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['num_bid', 'source_bid', 'recipient_bid', 'port_bid', 'protocol_bid', 'description_bid', 'justification_bid']
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
            'description_bid': Textarea(attrs={
                'placeholder': "Описание"
            }),
            'justification_bid': Textarea(attrs={
                'placeholder': "Обоснование"
            }),
            'port_bid': TextInput(attrs={
                'placeholder': "Порт"
            })

        }
