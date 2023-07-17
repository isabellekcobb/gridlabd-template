import requests

def get_zipcode(latitude, longitude, api_key):
    url = f'https://api.opencagedata.com/geocode/v1/json?q={latitude}%2C{longitude}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    # Check if the API request was successful
    if response.status_code == 200 and data.get('results'):
        # Extract the zip code from the API response
        zipcode = data['results'][0]['components']['postcode']
        return zipcode
    else:
        # Handle the error case
        error_message = data.get('status', 'Unknown error')
        print(f'Error: {error_message}')
        return None

# Provide your latitude, longitude, and API key
latitude = 37.7749
longitude = -122.4194
api_key = '9zS25U1TomaV3vQzgiAexB8eVaNV02HrrcmtBm0q'

zipcode = get_zipcode(latitude, longitude, api_key)
if zipcode:
    print(f'The zip code for the given latitude and longitude is {zipcode}.')
