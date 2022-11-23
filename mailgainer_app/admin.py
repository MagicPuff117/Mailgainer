# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mailgainer_app.models import Contact

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date', 'email']


admin.site.register(Contact, UserAdmin)
