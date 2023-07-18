import csv
import pandas as pd
from geopy.geocoders import Nominatim

# Function to convert latitude and longitude to zip code
def get_zipcode(lat, lon):
    geolocator = Nominatim(user_agent="zipcode_converter")
    location = geolocator.reverse((lat, lon), exactly_one=True)
    address = location.raw['address']
    zipcode = address.get('postcode', '')
    return zipcode

# Read latitude and longitude from CSV files
latitude = pd.read_csv('Latitude.csv')
longitude = pd.read_csv('Longitude.csv')

# Combine latitude and longitude into a coordinates array
coordinates = list(zip(latitude['Latitude'], longitude['Longitude']))

# Convert coordinates to zip codes
results = []
for lat, lon in coordinates:
    zipcode = get_zipcode(lat, lon)
    results.append((lat, lon, zipcode))

# Export results to a CSV file
filename = "zipcode_results.csv"
header = ["Latitude", "Longitude", "Zip Code"]
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(results)

print(f"Data exported to '{filename}' successfully.")
