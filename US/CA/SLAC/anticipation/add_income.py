import csv
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import time

def get_zipcode(lat, lon):
    geolocator = Nominatim(user_agent="zipcode_converter", timeout=10)  # Increased timeout to 10 seconds
    retries = 5  # Maximum number of retries
    location = None
    
    for _ in range(retries):
        try:
            location = geolocator.reverse((lat, lon), exactly_one=True)
            if location is not None and 'address' in location.raw:
                address = location.raw['address']
                if 'postcode' in address:
                    return address['postcode']
        except (GeocoderTimedOut, GeocoderUnavailable):
            # Retry after a delay
            time.sleep(2)
    
    return ""


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
