#!/usr/bin/env python3
#
# Create CSV of fake names and numbers for cell phones
#

import requests
import json
import random
from numpy.random import choice

headers="\"number\",\"name\",\"carrier\",\"devicetype\",\"country\""
names=[]

# Carriers and probobilities (needs to sum to 100%)
Carriers=['AT&T Mobility','Rogers Wireless [CAN]','Verizon Wireless']
Carriers_P=[0.45,0.1,0.45]
Country={'AT&T Mobility':'US','Rogers Wireless [CAN]':'Canada','Verizon Wireless':'US'}
# Device Types and probobilities (needs to sum to 100%)
DeviceType=['Basic Phone','Embedded Modem','Mobile Hotspot','Smartphone','Tablet','Unassigned','USB Modem']
DeviceType_P=[0.0004,0.02,0.014,0.86,0.10,0.005,0.0006]


# Get some random US Names,mixed gender, with phone numbers.  500 max request
# numbers are all US too, even though we are including Canada subscribers
for x in range(0,1):
    results=requests.get("https://uinames.com/api/?amount=500&ext&region=united+states")
    for item in results.json():
        names.append(item)

print(headers)
for item in names:
    carrier=choice(Carriers,1, p=Carriers_P)[0]    
    devicetype=choice(DeviceType,1, p=DeviceType_P)[0]
    country=Country[carrier]
    print("\"%s\",\"%s, %s\",\"%s\",\"%s\",\"%s\"" % (item['phone'],item['surname'],item['name'],carrier,devicetype,country))
