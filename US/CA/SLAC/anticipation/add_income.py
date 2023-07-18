import csv
import pandas as pd
import requests

def get_zipcode(lat, lon):
    username = 'isabellekcobb'  # Replace with your GeoNames username
    base_url = f'http://api.geonames.org/findNearbyPostalCodesJSON?lat={lat}&lng={lon}&username={username}'
    
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        if 'postalCodes' in data:
            postal_codes = data['postalCodes']
            if postal_codes:
                return postal_codes[0]['postalCode']
    
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


