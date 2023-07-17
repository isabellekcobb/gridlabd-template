import pandas as pd
import subprocess

# Provide your latitude, longitude
latitude = pd.read_csv('latitude.csv')['latitude'].tolist()
longitude = pd.read_csv('longitude.csv')['longitude'].tolist()

command = 'gridlabd geodata merge -D census {}'

output_file = '/path/to/output/test_zipcode.csv'

# Iterate over latitude and longitude pairs and execute the census subcommand for each
for lat, lon in zip(latitude, longitude):
    formatted_command = command.format(f'{lat},{lon}')
    subprocess.run(formatted_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print(f'Output appended for latitude: {lat}, longitude: {lon}')
