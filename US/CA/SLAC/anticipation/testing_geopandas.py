import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

def get_zipcode_geopandas(latitude_file, longitude_file, geojson_file, output_csv_file):
    # Read latitude and longitude from CSV files
    latitude_df = pd.read_csv(latitude_file)
    longitude_df = pd.read_csv(longitude_file)

    # Create a list of latitude and longitude pairs
    coordinates = zip(latitude_df['latitude'], longitude_df['longitude'])

    # Read the GeoJSON file into a GeoDataFrame
    gdf = gpd.read_file(geojson_file)

    zipcodes = []
    # Iterate through each latitude and longitude pair
    for lat, lon in coordinates:
        point = Point(lon, lat)
        zipcode = None

        # Check if the point is within any polygon (zipcode boundary)
        for idx, row in gdf.iterrows():
            if point.within(row['geometry']):
                zipcode = row['ZIP_CODE']
                break

        zipcodes.append(zipcode)

    # Create a new DataFrame with zip codes
    result_df = pd.DataFrame({'latitude': latitude_df['latitude'], 'longitude': longitude_df['longitude'], 'address': zipcodes})

    # Read income data from CSV file and merge with zipcodes
    income = pd.read_csv("income_CA.csv")
    merged_df=pd.merge(result_df, income, on="address", how="inner", sort=True)
    merged_df.to_csv("merged_results.csv", index=False)
    

# Example usage:
latitude_file = "latitude.csv"  # Replace with the path to your latitude CSV file
longitude_file = "longitude.csv"  # Replace with the path to your longitude CSV file
geojson_file = "USA_ZIP_Code_Boundaries.geojson"  # Replace with the path to your GeoJSON file
output_csv_file = "output_zipcodes.csv"  # Replace with the desired output CSV file path

get_zipcode_geopandas(latitude_file, longitude_file, geojson_file, output_csv_file)
