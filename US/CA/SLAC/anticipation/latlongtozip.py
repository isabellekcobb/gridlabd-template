import pandas as pd
import subprocess

# Provide your latitude, longitude
latitude = pd.read_csv('latitude.csv')['latitude'].tolist()
longitude = pd.read_csv('longitude.csv')['longitude'].tolist()

command = 'gridlabd geodata merge -D census {}'

output_file = '$OPENFIDO_OUTPUT/test_zipcode.csv'

# Iterate over latitude and longitude pairs and execute the census subcommand for each
for lat, lon in zip(latitude, longitude):
    formatted_command = command.format(f'{lat},{lon}')
    
    # Execute the command and capture the output
    completed_process = subprocess.run(formatted_command, shell=True, capture_output=True, text=True)
    command_output = completed_process.stdout
    
    # Append the output to the output file
    with open(output_file, 'a') as file:
        file.write(command_output)
