import pandas as pd

# Read the CSV file and use the 'status' column as the sort key
csv_input = pd.read_csv('path_result_plot.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike', 'status'])

# Sort the DataFrame for "FAILED" status rows in descending order based on the 'strike' column
failed_rows = csv_input[csv_input['status'] == 'FAILED']
failed_rows.sort_values(by='strike', ascending=False, inplace=True)

# Sort the DataFrame for "OK" status rows in descending order based on the 'strike' column
ok_rows = csv_input[csv_input['status'] == 'OK']
ok_rows.sort_values(by='strike', ascending=False, inplace=True)

# Concatenate the sorted DataFrames to combine the "FAILED" and "OK" status rows
sorted_csv_input = pd.concat([failed_rows, ok_rows])

# Now the 'sorted_csv_input' DataFrame will have "FAILED" status rows sorted by 'strike' in descending order,
# and the "OK" status rows sorted by 'strike' in descending order, with "FAILED" ones above "OK" ones.
sorted_csv_input.to_csv('prioritization.csv', index=False)
