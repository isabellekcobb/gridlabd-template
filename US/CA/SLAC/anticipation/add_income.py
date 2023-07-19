import csv
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import time
import requests

def get_zipcode(lat, lon, api_key):
    base_url = "http://dev.virtualearth.net/REST/v1/Locations"
    query_params = {
        "key": api_key,
        "includeEntityTypes": "Postcode1",
        "c": f"{lat},{lon}",
        "o": "json"
    }
    
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
        data = response.json()
        if "resourceSets" in data and data["resourceSets"]:
            results = data["resourceSets"][0]["resources"]
            if results:
                address = results[0]["address"]
                if "postalCode" in address:
                    return address["postalCode"]
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    
    return ""

bing_maps_api_key = "AiCmdQvtGYgBidB1BVvGfHPIGrxLwGQ0K8fAeWFRNVZqsqtXLoZgRmbw6V-ZTPiA"

# Read latitude and longitude from CSV files
latitude = pd.read_csv('latitude.csv')
longitude = pd.read_csv('longitude.csv')

# Combine latitude and longitude into a coordinates array
coordinates = list(zip(latitude['latitude'], longitude['longitude']))

# Convert coordinates to zip codes
results = []
for lat, lon in coordinates:
    zipcode = get_zipcode(lat, lon, bing_maps_api_key)
    if not zipcode:
        zipcode = 'N/A'  # Assign a default value for missing zip codes
    results.append((lat, lon, zipcode))

# Create DataFrame from the results
df = pd.DataFrame(results, columns=["latitude", "longitude", "zipcode"])

df.to_csv('results.csv',index=False)

# Read income data from CSV file
income = pd.read_csv("income_CA.csv")

# Perform inner join on Zip Code to combine income data
merged_df = pd.merge(df, income, on="zipcode", how="inner")

# Export merged DataFrame to a CSV file
filename = "merged_results.csv"
merged_df.to_csv(filename, index=False)

print(f"Data exported to '{filename}' successfully.")
