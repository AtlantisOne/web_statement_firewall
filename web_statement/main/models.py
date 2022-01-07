from django.db import models
from django.contrib.auth.models import User
from web_statement import settings


class Bid(models.Model):
    created_date_bid = models.DateTimeField('Дата создания заявки', auto_now_add=True)
    modified_date_bid = models.DateTimeField('Дата изменения заявки', auto_now=True)
    num_bid = models.TextField('Заявка', null=True, blank=True)
    status_bid = models.ForeignKey('Status_bid_class', on_delete=models.CASCADE, null=True, blank=True)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='User')
    persistent_rule = models.BooleanField('Постоянное правило', default=True)
    date_rule_start = models.DateField('Дата начала действия', null=True, blank=True)
    date_rule_end = models.DateField('Дата окончания действия', null=True, blank=True)
    justification_bid = models.TextField('Обоснование', default='Обоснование')
    description_bid = models.TextField('Описание', default='Описание')
    user_phone_bid = models.TextField('Телефон исполнителя', default='8-3532-000000', null=True, blank=True)
    user_department_name_bid = models.TextField('Наименование СП исполнителя', default='Наименование СП исполнителя',
                                                null=True, blank=True)
    boss_department_name_bid = models.TextField('Наименование СП руководителя', default='Наименование СП руководителя',
                                                null=True, blank=True)
    boss_full_name_bid = models.TextField('Фамилия И.О. руководителя', default='Фамилия И.О. руководителя', null=True,
                                          blank=True)

    def get_persistent_rule(self):
        if self.persistent_rule == True:
            return 'Постоянно'
        return 'Временно'

    def get_date_rule_start(self):
        if self.date_rule_start == None:
            return '«___» _____________ 20__г.'
        date_str = str(self.date_rule_start)
        return f'« {date_str[8:10]} »   {date_str[5:7]}   {date_str[0:4]}г.'

    def get_date_rule_end(self):
        if self.date_rule_end == None:
            return '«___» _____________ 20__г.'
        date_str = str(self.date_rule_end)
        return f'« {date_str[8:10]} »   {date_str[5:7]}   {date_str[0:4]}г.'

    def __str__(self):
        return f'{self.num_bid}'

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Protocol_bid_class(models.Model):
    title = models.CharField('Тип протокола', max_length=300)

    def __str__(self):
        return self.title


class Status_bid_class(models.Model):
    title = models.CharField('Статус заявки', max_length=300)

    def __str__(self):
        return self.title

class Rule(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.SET_NULL, null=True, blank=True)
    # source_bid = models.GenericIPAddressField('Источник', default='192.168.0.1')
    # recipient_bid = models.GenericIPAddressField('Получатель', default='192.168.0.2')
    port_bid = models.IntegerField('Порт', default='3389')
    protocol_bid = models.ForeignKey('Protocol_bid_class', on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.bid}'


class SourceBid(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.SET_NULL, null=True, blank=True)
    source_bid = models.GenericIPAddressField('Источник', default='192.168.0.1')

    def __str__(self):
        return f'{self.bid}'


class RecipientBid(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.SET_NULL, null=True, blank=True)
    recipient_bid = models.GenericIPAddressField('Получатель', default='192.168.0.2')

    def __str__(self):
        return f'{self.bid}'


class Signers_bid(models.Model):
    role = models.ForeignKey('Signer_role', on_delete=models.CASCADE, )
    position = models.CharField('Должность согласующего', max_length=300)
    full_name = models.CharField('ФИО согласующего', max_length=50)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, )

    def __str__(self):
        return self.position


class Organization(models.Model):
    title = models.CharField('Организация', max_length=100)

    def __str__(self):
        return self.title


class Signer_role(models.Model):
    title = models.CharField('Роль в согласовании', max_length=100)

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
