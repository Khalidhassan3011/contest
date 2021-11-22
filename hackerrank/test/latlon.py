# Scrap time 2021-01-10 4:18 pM
# If any one Scrap with this project you need to update as website updated format

# import necessary lib
import geolocator as geolocator
import requests
import time
import math
# import pandas as pd
import re
import csv

from random import randint
from datetime import datetime
import pandas as pd

# To read 6th row data
data = pd.read_csv("C:/Users/KhaliD HassaN/Desktop/New folder/test.csv", )
csv_file = 'evaly_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M')) + '.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        'lat',
        'long',
        'city',
        'state',
        'country'
    ]
                            )
    writer.writeheader()

# To print the values
print(data)

# To convert values into list
list_value = data.values.tolist()
i = 0
for i in range(8):
    # Latitude and Longitude
    latitude = list_value[i][0]
    longitude = list_value[i][1]
    print(latitude)
    print(longitude)

    location = geolocator.reverse(latitude + "," + longitude)
    address = location.raw['address']

    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print('City : ', city)
    print('State : ', state)
    print('Country : ', country)
    print('Zip Code : ', zipcode)
    row = {
        'lat': latitude,
        'long': longitude,
        'city': city,
        'state': state}
    print(row)
    # submission.to_csv('submission.csv', index=False)
    writer.writerow([row])
