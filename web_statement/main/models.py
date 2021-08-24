from django.db import models
from django.contrib.auth.models import User


class Bid(models.Model):
    created_date_bid = models.DateTimeField('Дата создания заявки', auto_now_add=True)
    modified_date_bid = models.DateTimeField('Дата изменения заявки', auto_now=True)
    num_bid = models.AutoField(primary_key=True)
    auth_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    source_bid = models.GenericIPAddressField('Источник', default='192.168.0.1')
    recipient_bid = models.GenericIPAddressField('Получатель', default='192.168.0.2')
    port_bid = models.IntegerField('Порт', default='3389')
    protocol_bid = models.ForeignKey('Protocol_bid_class', on_delete=models.CASCADE, )
    persistent_rule = models.BooleanField('Постоянное правило', default=True)
    date_rule_start = models.DateField('Дата начала действия', null=True, blank=True)
    date_rule_end = models.DateField('Дата окончания действия', null=True, blank=True)
    justification_bid = models.TextField('Обоснование', default='Обоснование')
    description_bid = models.TextField('Описание', default='Описание')

    def __str__(self):
        return self.num_bid

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Protocol_bid_class(models.Model):
    title = models.CharField('Тип протокола', max_length=300)

    def __str__(self):
        return self.title

    # from django.utils import timezone

    # class User(models.Model):
    #     created     = models.DateTimeField(editable=False)
    #     modified    = models.DateTimeField()
    #
    #     def save(self, *args, **kwargs):
    #         ''' On save, update timestamps '''
    #         if not self.id:
    #             self.created = timezone.now()
    #         self.modified = timezone.now()
    #         return super(User, self).save(*args, **kwargs)
