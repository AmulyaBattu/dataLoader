import os
import random
import string
from datetime import datetime

from dl.models import userData, userCart, userDataTypes
from django.db import models



def generate_randomInteger():
    return random.randint(1, 100)

def generate_randomString(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def generate_randomDate():
    year = random.randint(1950, 2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return datetime(year, month, day).strftime('%Y-%m-%d')

def generate_randomBinary(size=0):
    return os.urandom(size)

def generate_randomEmail(count = 1):
    return [generate_randomString(7) + '@' + generate_randomDomain() for i in range(count)]

def generate_randomDomain():
    domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
    return random.choice(domains)


def getUserData():
    column = []
    columnDict = {}
    fieldDict ={}
    model = str(userData._meta.app_label + '.' + userData._meta.model_name)
    columnDict.update({'model':model})

    for item in userData._meta.fields:
        if isinstance(item, models.IntegerField):
            column.append(generate_randomInteger())
            columnDict.update({'pk': generate_randomInteger()})

        elif isinstance(item, models.CharField):
            column.append(generate_randomString())
            fieldDict.update({'name': generate_randomString()})

        elif isinstance(item, models.DateField):
            column.append(generate_randomDate())
            fieldDict.update({'dob': generate_randomDate()})

    columnDict.update({'fields': fieldDict})
    return [column, columnDict]

def getUserItemData():
    cart = []
    cartDict = {}
    fieldDict ={}
    model = str(userCart._meta.app_label + '.' + userCart._meta.model_name)
    cartDict.update({'model':model})
    for item in userCart._meta.fields:

        if isinstance(item, models.IntegerField):
            cart.append(random.randint(1,5))
            fieldDict.update({'items': random.randint(1,5) })

        elif isinstance(item, models.CharField):

            if len(cart) == len(userCart._meta.fields)- 3:
                itemPrice = []
                for i in range(cart[0]):
                    itemPrice.append(str(random.uniform(10.0, 25.06)))
                itemcost = ','.join(itemPrice)
                cart.append(itemcost)
                fieldDict.update({'itemPrice': itemcost})

            else:
                itemList = []
                for i in range(cart[0]):
                    itemList.append(generate_randomString())
                items = ','.join(itemList)
                cart.append(str(items))
                fieldDict.update({'itemList': str(items)})

        elif isinstance(item, models.FloatField):

            if len(cart) == len(userCart._meta.fields)- 2:
                priceList = []
                for item in cart[2].split(','):
                    priceList.append(float(item))
                cart.append(sum(priceList))
                fieldDict.update({'totalCost':sum(priceList)})
    cartDict.update({'fields':fieldDict})
    return [cart, cartDict]

def getUserDataTypes():
    dataTypes = []
    dataTypesDict = {}
    fieldDict = {}
    model = str(userDataTypes._meta.app_label + '.' + userDataTypes._meta.model_name)
    dataTypesDict.update({'model':model})
    for item in userDataTypes._meta.fields:
        if isinstance(item, models.BinaryField):
            blob = generate_randomBinary(1024)
            dataTypes.append(blob)
            fieldDict.update({'images': blob})

        if isinstance(item, models.EmailField):
            emails = generate_randomEmail(1)
            #emails = ','.join(email)
            dataTypes.append(emails)
            fieldDict.update({'email': emails})

    dataTypesDict.update({'fields':fieldDict})
    return [dataTypes, dataTypesDict]


