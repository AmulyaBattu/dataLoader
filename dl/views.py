# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from .models import userData, userCart, userDataTypes
import script
from django.shortcuts import render

def insertData(request):

    for i in range(6):
        column = script.getUserData()
        user_instance = userData.objects.create(name=column[0], dob = column[1])

        cart = script.getUserItemData()
        item_instance = userCart.objects.create(items=cart[0], itemList=cart[1], itemPrice=cart[2], totalCost=cart[3])

        dataTypes = script.getUserDataTypes()
        data_instance = userDataTypes.objects.create(images=dataTypes[0], email=dataTypes[1])

    line1 = str(i) + 'rows inserted in user cart table !!'
    line2 = str(i) + ' rows inserted in user table!!'
    line3 = str(i) + ' rows inserted in userDataType table!!'
    return HttpResponse(line1 + '\n' +line2 + '\n' +line3)
