import csv
import pandas as pd
import time
from geopy.geocoders import Nominatim

# Function to convert latitude and longitude to zip code
def get_zipcode(lat, lon):
    geolocator = Nominatim(user_agent="zipcode_converter")
    time.sleep(1)  # Add a delay of 1 second
    location = geolocator.reverse((lat, lon), exactly_one=True)
    address = location.raw['address']
    zipcode = address.get('postcode', '')
    return zipcode

# Convert coordinates to zip codes
results = []
for lat, lon in coordinates:
    zipcode = get_zipcode(lat, lon)
    if not zipcode:
        zipcode = 'N/A'  # Assign a default value for missing zip codes
    results.append((lat, lon, zipcode))
