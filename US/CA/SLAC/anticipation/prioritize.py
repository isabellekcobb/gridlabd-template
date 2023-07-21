import pandas as pd

# Read the CSV file and use the 'status' column as the sort key
csv_input = pd.read_csv('path_result_plot.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike', 'status'])

# Sort the DataFrame by the 'status' column in ascending order
csv_input.sort_values(by='status', ascending=True, inplace=True)

# Now the 'csv_input' DataFrame will have rows with "FAILED" status at the top and "OK" status at the bottom
csv_input.to_csv('sorted_path_result.csv', index=False)
