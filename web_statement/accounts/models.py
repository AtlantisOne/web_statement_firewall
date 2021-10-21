from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=150, blank=True, null=True)
    user_phone = models.CharField('Телефон', max_length=20, blank=True, null=True)

    def get_full_name(self):
        full_name = '%s %s. %s.' % (self.last_name, self.first_name[0], self.middle_name[0])
        return full_name.strip()
