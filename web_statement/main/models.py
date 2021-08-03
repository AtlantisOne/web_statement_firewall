from django.db import models
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

class Bid(models.Model):
    created_date_bid = models.DateTimeField('Дата создания заявки', auto_now_add=True)
    modified_date_bid = models.DateTimeField('Дата изменения заявки', auto_now=True)
    num_bid = models.CharField('Номер заявки', max_length=250, default='ОР-')
    source_bid = models.GenericIPAddressField('Источник')
    recipient_bid = models.GenericIPAddressField('Получатель')
    port_bid = models.IntegerField('Порт', default='0')
    protocol_bid = models.CharField('Протокол', max_length=300, default='TCP')
    description_bid = models.TextField('Описание')
    time_rule = models.CharField('Тип правила: постоянное/временное', max_length=300, default='Постоянное')
    date_rule_start = models.DateField('Дата начала действия')
    date_rule_end = models.DateField('Дата окончания действия')
    justification_bid = models.TextField('Обоснование')


    def __str__(self):
        return self.num_bid

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'



# Create your models here.
