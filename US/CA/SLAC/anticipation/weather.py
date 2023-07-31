import pandas as pd
import requests

def get_nsrdb_data(latitude, longitude):
    url = f'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-tmy2?api_key=MvtWm50sLgUCxfkZcgOfOLATc7cA6wo5fsxJ7b2y&lat={latitude}&lon={longitude}&year=2022'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch NSRDB data for latitude {latitude} and longitude {longitude}.")
        return None

def main():
    excel_file = 'gps.xlsx'

    # Replace 'Sheet1' with the name of the sheet containing the data
    # df = pd.read_excel(excel_file)
    # gps_points = df['GPS Point']


    for point in gps_points:
        # Split latitude and longitude from "latitude,longitude" string
        # latitude, longitude = map(float, point.split(','))
        latitude=34.4002833340685
        longitude=-116.962349732192

        # Get NSRDB data for the given latitude and longitude
        data = get_nsrdb_data(latitude, longitude)

        # Do something with the NSRDB data
        # For example, print the data for now
        if data:
            print(f"NSRDB Data for latitude {latitude}, longitude {longitude}:")
            print(data)
main()
