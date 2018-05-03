import os
import random
import string
from datetime import datetime

from dl.models import userData, userCart, userDataTypes
from django.db import models

column = []

def generate_randomInteger():
    return random.randint(1, 100)

def generate_randomString(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def generate_randomDate():
    year = random.randint(1950, 2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return datetime(year, month, day)

def generate_randomBinary(size=0):
    return os.urandom(size)

def generate_randomEmail(count = 1):
    return [generate_randomString(7) + '@' + generate_randomDomain() for i in range(count)]

def generate_randomDomain():
    domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
    return random.choice(domains)


def getUserData():

    for item in userData._meta.fields:
        if isinstance(item, models.IntegerField):
            column.append(generate_randomInteger())

        elif isinstance(item, models.CharField):
            column.append(generate_randomString())

        elif isinstance(item, models.DateField):
            column.append(generate_randomDate())

    return column

def getUserItemData():
    cart = []

    for item in userCart._meta.fields:

        if isinstance(item, models.IntegerField):
            cart.append(random.randint(1,5))

        elif isinstance(item, models.CharField):

            if len(cart) == len(userCart._meta.fields)- 3:
                itemPrice = []
                for i in range(cart[0]):
                    itemPrice.append(str(random.uniform(10.0, 25.06)))
                itemcost = ','.join(itemPrice)
                cart.append(itemcost)

            else:
                itemList = []
                for i in range(cart[0]):
                    itemList.append(generate_randomString())
                items = ','.join(itemList)
                cart.append(str(items))

        elif isinstance(item, models.FloatField):

            if len(cart) == len(userCart._meta.fields)- 2:
                priceList = []
                for item in cart[2].split(','):
                    priceList.append(float(item))
                cart.append(sum(priceList))

    return cart

def getUserDataTypes():
    dataTypes = []

    for item in userDataTypes._meta.fields:
        if isinstance(item, models.BinaryField):
            blob = generate_randomBinary(1024)
            dataTypes.append(blob)

        if isinstance(item, models.EmailField):
            emails = generate_randomEmail(1)
            #emails = ','.join(email)
            dataTypes.append(emails)

    return dataTypes


