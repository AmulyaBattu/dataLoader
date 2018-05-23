# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from .models import userData, userCart, userDataTypes
import script
from django.shortcuts import render
import json
import base64
import ast

userlist = []

def insertAndDeleteData(request):

    for i in range(6):
        userDict = script.getUserData()[1]
        userDict.update({'pk': i + 1})
        userlist.append(userDict)

        userCartDict = script.getUserItemData()[1]
        userCartDict.update({'pk': i + 1})
        userlist.append(userCartDict)

        userDataTypesDict = script.getUserDataTypes()[1]
        userDataTypesDict.update({'pk': i + 1})
        userlist.append(userDataTypesDict)

    for item in userlist:
        if 'images' in item['fields'].keys():
            item['fields']['images'] = base64.b64encode(item['fields']['images'])

    ## writing to a JSON FILE
    with open('dl/fixtures/data.json', 'wb') as dataFile:
        json.dump(userlist, dataFile)

    ## reading from a JSON FILE
    with open('dl/fixtures/data.json', 'rb') as dataFile:
       data = json.loads(dataFile.read())

    for item in data:
        if 'images' in item['fields'].keys():
            item['fields']['images'] = base64.b64decode(item['fields']['images'])
        ## Inserting data into the database
        if item['model'] == 'dl.userdata':
            userData.objects.create(pk=item['pk'], name=item['fields']['name'], dob=item['fields']['dob'])
        elif item['model'] == 'dl.usercart':
            userCart.objects.create(pk=item['pk'], items=item['fields']['items'], itemList=item['fields']['itemList'],
                                    itemPrice=item['fields']['itemPrice'], totalCost=item['fields']['totalCost'])
        elif item['model'] == 'dl.userdatatypes':
            userDataTypes.objects.create(pk=item['pk'], images=item['fields']['images'], email=item['fields']['email'])

    line1 = 'Data is written to file and DB'


    ## deleting everything from File and DB
    file = open('dl/fixtures/data.json', 'r+')
    file.truncate()
    userData.objects.all().delete()
    userCart.objects.all().delete()
    userDataTypes.objects.all().delete()
    line2 = 'Data deleted from Json File and Database!!'


    return HttpResponse(line1 + '\n' + line2 )

