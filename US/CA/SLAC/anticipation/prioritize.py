import pandas as pd

# Read the CSV file and use the 'status' column as the sort key
csv_input = pd.read_csv('path_result_plot.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike', 'status','income'])

strike = csv_input['strike']
contact = csv_input['contact']
income = csv_input['income']

strike_pts = pd.Series()
# Iterate through all the values in strike, multiply them by 10, and append to the new Series
for index, value in strike.items():
    strike_pts[index] = value * 10

contact_pts = pd.Series()
# Iterate through all the values in contact, multiply them by 7, and append to the new Series
for index, value in contact.items():
    contact_pts[index] = value * 7

# Find the highest income value 
highest_income_value = income.max()
income_pts = pd.Series()
for index, value in income.items():
    if value<=0.5*highest_income_value:
        income_pts[index] = 5
    elif value<=0.6*highest_income_value:
        income_pts[index] = 4
    elif value<=0.7*highest_income_value:
        income_pts[index] = 3
    else:
        income_pts[index] = 0

total_pts=strike_pts+contact_pts+income_pts

# Append the total_pts to the path_result_plot file with a custom header
total_pts.to_csv('path_result_plot.csv', header=['Criticality'], mode='a')
    

