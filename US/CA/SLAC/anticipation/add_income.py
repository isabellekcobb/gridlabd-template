import csv
import pandas as pd
import requests
import time
from geopy.geocoders import Nominatim

# Function to convert latitude and longitude to zip code
def get_zipcode(lat, lon):
    geolocator = Nominatim(user_agent="zipcode_converter")
    time.sleep(2)  # Add a delay of 2 seconds
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
header = ["Latitude", "Longitude", "Zip Code"]
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(results)

# Create DataFrame from the results
df = pd.DataFrame(results, columns=["latitude", "longitude", "zipcode"])

# Read income data from CSV file
income = pd.read_csv("income_CA.csv")

# Perform inner join on Zip Code to combine income data
merged_df = pd.merge(df, income, on="zipcode", how="inner")

# Export merged DataFrame to a CSV file
filename = "merged_results.csv"
merged_df.to_csv(filename, index=False)

print(f"Data exported to '{filename}' successfully.")


