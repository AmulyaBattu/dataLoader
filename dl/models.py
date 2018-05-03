# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class userData(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField(max_length=10)

class userCart(models.Model):
    items = models.IntegerField()
    itemList = models.CharField(max_length=100)
    itemPrice = models.CharField(max_length=100)
    totalCost = models.FloatField(max_length=500)

class userDataTypes(models.Model):
    images = models.BinaryField()
    email = models.EmailField(max_length=100)
