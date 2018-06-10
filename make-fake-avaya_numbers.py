#!/usr/bin/env python3
#
# Create CSV of fake names and numbers for Avaya phones
#

import requests
from numpy.random import choice

headers = "\"Extension\",\"Name\",\"Type\",\"Room\",\"Floor\",\"Building\""
names = []
base = 235000

# Device Types and probobilities (needs to sum to 100%)
DeviceType = ['2410', '9620', '9611', \
              'softIP', 'poly', '1608', \
              '2420', 'softd', 'fax']
DeviceType_P = [0.36, 0.22, 0.13, 0.11, 0.08, 0.03, 0.03, 0.02, 0.02]

ROOM = ['conf-a', 'conf-b', 'North', 'South', 'West', \
        'East', 'Team Room-A', 'Team Room-B']
ROOM_P = [0.1, 0.1, 0.15, 0.15, 0.15, 0.15, 0.1, 0.1]
FLOOR = [1, 2, 3, 4]
FLOOR_P = [0.25, 0.25, 0.25, 0.25]
BLDG = ['Downtown', 'HQ', 'Manufacturing', 'Showroom', 'Chicago', 'NYC']
BLDG_P = [0.25, 0.25, 0.20, 0.20, 0.05, 0.05]


# Get some random US Names,mixed gender, with phone numbers.  500 max request
# numbers are all US too, even though we are including Canada subscribers
for x in range(0, 1):
    results = requests.get("https://uinames.com/api/?amount=500&ext&region=united+states")
    for item in results.json():
        names.append(item)

print(headers)
for item in names:
    devicetype = choice(DeviceType, 1, p=DeviceType_P)[0]
    print("\"%s\",\"%s %s\",\"%s\",\"%s\",\"%s\",\"%s\"" % (base,\
            item['name'], item['surname'], devicetype, \
            choice(ROOM, 1, p=ROOM_P)[0], \
            choice(FLOOR, 1, p=FLOOR_P)[0], \
            choice(BLDG, 1, p=BLDG_P)[0]))
    base += 1
