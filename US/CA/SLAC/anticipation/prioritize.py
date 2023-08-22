import pandas as pd
import re

# Read the CSV file and use the 'status' column as the sort key
csv_input = pd.read_csv('path_result_plot.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike', 'status','income'])

strike = csv_input['strike']
contact = csv_input['contact']
income = csv_input['income']
lat = csv_input['latitude']
lon = csv_input['longitude']

length=len(csv_input['strike'])
strike_pts = pd.Series(0, index=range(length))
# Iterate through all the values in strike, multiply them by 10, and append to the new Series
for index, value in strike.items():
    strike_pts[index] = value * 10

contact_pts = pd.Series(0, index=range(length))
# Iterate through all the values in contact, multiply them by 7, and append to the new Series
for index, value in contact.items():
    contact_pts[index] = value * 7

# Find the highest income value 
highest_income_value = income.max()
income_pts = pd.Series(0, index=range(length))
for index, value in income.items():
    if value<=0.5*highest_income_value:
        income_pts[index] = 5
    elif value<=0.6*highest_income_value:
        income_pts[index] = 4
    elif value<=0.7*highest_income_value:
        income_pts[index] = 3
    else:
        income_pts[index] = 0

# critical loading

def parse_glm_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    objects = re.findall(r'\{([^}]*)\}', data)
    object_dicts = []

    for obj in objects:
        obj_data = {}
        lines = obj.strip().split('\n')
        for line in lines:
            key, value = map(str.strip, line.split(':', 1))
            obj_data[key] = value
        object_dicts.append(obj_data)

    return object_dicts

def extract_lat_lon(obj_data):
    latitude = obj_data.get('latitude', None)
    longitude = obj_data.get('longitude', None)
    return latitude, longitude

latlong_list = parse_glm_file('critical_data.glm')
    
load_pts = pd.Series(0, index=range(length))
csv_input['critical load'] = [False] * length
loads = csv_input['critical load']

for obj_data in latlong_list:
    latitude, longitude = extract_lat_lon(obj_data)
    for index, value in loads.items():
        if lat[index]==latitude and lon[index]==longitude:
            loads[index]=True

# Assign poles attached to critical loads a critical value of 5, leave all others with zero point value
for index, value in loads.items():
    if value == True:
        load_pts[index]=5
    

total_pts=strike_pts+contact_pts+income_pts+load_pts

# Append the total_pts to the path_result_plot file with a custom header and sort by criticality
csv_input['criticality'] = total_pts
csv_sorted = csv_input.sort_values(by='criticality', ascending=False)

# Write the updated DataFrame back to the CSV file, including the new column
csv_sorted.to_csv('path_result_plot.csv', index=False)
    

