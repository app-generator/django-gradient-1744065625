# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Products(models.Model):

    #__Products_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    createdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Budget(models.Model):

    #__Budget_FIELDS__
    client = models.IntegerField(null=True, blank=True)
    createdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updatedate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    validationdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Budget_FIELDS__END

    class Meta:
        verbose_name        = _("Budget")
        verbose_name_plural = _("Budget")


class Budget_Item(models.Model):

    #__Budget_Item_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    value = models.TextField(max_length=255, null=True, blank=True)

    #__Budget_Item_FIELDS__END

    class Meta:
        verbose_name        = _("Budget_Item")
        verbose_name_plural = _("Budget_Item")


class Expenses(models.Model):

    #__Expenses_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    duedate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    createdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    value = models.TextField(max_length=255, null=True, blank=True)

    #__Expenses_FIELDS__END

    class Meta:
        verbose_name        = _("Expenses")
        verbose_name_plural = _("Expenses")



#__MODELS__END
