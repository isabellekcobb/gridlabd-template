import subprocess
import csv
import pandas as pd

def gridlabd_geodata_merge(location1, location2, output_file):
    cmd = f"gridlabd geodata merge -D distance location {location1} {location2}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()

    if process.returncode == 0:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Location 1", "Location 2", "Result"])
            writer.writerow([location1, location2, output.decode().strip()])
        print(f"Results written to '{output_file}' successfully.")
    else:
        print("Error executing gridlabd geodata merge.")

# Read latitude and longitude from CSV files
latitude = pd.read_csv('latitude.csv')
longitude = pd.read_csv('longitude.csv')

# Combine latitude and longitude into a coordinates array
coordinates = list(zip(latitude['latitude'], longitude['longitude']))

output_file='results.csv'
# Convert coordinates to zip codes
results = []
for lat, lon in coordinates:
    zipcode = gridlabd_geodata_merge(lat, lon, output_file)
    if not zipcode:
        zipcode = 'N/A'  # Assign a default value for missing zip codes
    results.append((lat, lon, zipcode))

df = pd.DataFrame(results, columns=["latitude", "longitude", "zipcode"])

# Read income data from CSV file
income = pd.read_csv("income_CA.csv")

# Perform inner join on Zip Code to combine income data
merged_df = pd.merge(df, income, on="zipcode", how="inner")

# Export merged DataFrame to a CSV file
filename = "merged_results.csv"
merged_df.to_csv(filename, index=False)

print(f"Data exported to '{filename}' successfully.")

