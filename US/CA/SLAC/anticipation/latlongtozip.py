import pandas as pd
import subprocess

# Provide your latitude, longitude
latitude = pd.read_csv('latitude.csv')
longitude = pd.read_csv('longitude.csv')

command = 'gridlabd geodata merge -D census {} -o $OPENFIDO_OUTPUT/test_zipcode.csv'

# Iterate over latitude and longitude pairs and execute the census subcommand for each
for lat, lon in zip(latitude, longitude):
    formatted_command = command.format(f'{lat},{lon}')
    subprocess.run(formatted_command, shell=True)
