# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Contact(models.Model):

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['id']

    first_name = models.CharField(verbose_name='Имя',max_length=30, null=False)
    last_name = models.CharField(verbose_name='Фамилия',max_length=30)
    birth_date = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name




