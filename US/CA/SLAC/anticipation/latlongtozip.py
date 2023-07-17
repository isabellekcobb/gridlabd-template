import os
import pandas as pd
import subprocess

# Provide your latitude, longitude
latitude = pd.read_csv('latitude.csv')['latitude'].tolist()
longitude = pd.read_csv('longitude.csv')['longitude'].tolist()

command = 'gridlabd geodata merge -D census {}'

output_directory = '$OPENFIDO_OUTPUT'
output_file = 'test_zipcode.csv'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate over latitude and longitude pairs and execute the census subcommand for each
for lat, lon in zip(latitude, longitude):
    formatted_command = command.format(f'{lat},{lon}')
    
    # Execute the command and capture the output
    completed_process = subprocess.run(formatted_command, shell=True, capture_output=True, text=True)
    command_output = completed_process.stdout
    
    # Append the output to the output file
    output_path = os.path.join(output_directory, output_file)
    with open(output_path, 'a') as file:
        file.write(command_output)
