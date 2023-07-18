import csv
import pandas as pd
from geopy.geocoders import Nominatim

print("imports working",flush=True)

# Function to convert latitude and longitude to zip code
def get_zipcode(lat, lon):
    geolocator = Nominatim(user_agent="zipcode_converter")
    location = geolocator.reverse((lat, lon), exactly_one=True)
    address = location.raw['address']
    zipcode = address.get('postcode', '')
    return zipcode

# Read latitude and longitude from CSV files
latitude = pd.read_csv('latitude.csv')
longitude = pd.read_csv('longitude.csv')

# Combine latitude and longitude into a coordinates array
coordinates = list(zip(latitude['latitude'], longitude['longitude']))

# Convert coordinates to zip codes
results = []
for lat, lon in coordinates:
    zipcode = get_zipcode(lat, lon)
    if not zipcode:
        zipcode = 'N/A'  # Assign a default value for missing zip codes
    results.append((lat, lon, zipcode))

# Export results to a CSV file
filename = "zipcode_results.csv"
header = ["latitude", "longitude", "zip code"]
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(results)

# load the income data
# Source: https://www.psc.isr.umich.edu/dis/census/HCT012.csv
print(f"Loading income data...",end='',flush=True)
income = pd.read_csv("income_CA.csv")
print("ok",flush=True)

zip_only=pd.read_csv('zipcode_results.csv')

# add the income data
# TODO: add other states
print(f"Adding income data...",end='',flush=True)
zip_income = zip_only.join(income,how="inner",on="zip code",sort=True)
print("ok",flush=True)

zip_income.to_csv('income_result.csv', index=False)


