import pandas as pd

# Read the CSV file and use the 'status' column as the sort key
csv_input = pd.read_csv('path_result_plot.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike', 'status','income'])

# Sort the DataFrame for "FAILED" status rows in descending order based on the 'strike' column
failed_rows = csv_input[csv_input['status'] == 'FAILED']
failed_rows.sort_values(by='strike', ascending=False, inplace=True)

# Find the lowest income value and highlight failed_rows with that value
lowest_income_value = failed_rows['income'].min()
def highlight_cells(value, color_true, color_false, criteria):
 if value <= criteria:
     color = color_true 
 else:
     color = color_false 
 return 'background-color: {}'.format(color)
failed_rows.style.applymap(highlight_cells, color_true = 'yellow', color_false = 'white', criteria = lowest_income_value)

# Sort the DataFrame for "OK" status rows in descending order based on the 'strike' column
ok_rows = csv_input[csv_input['status'] == 'OK']
ok_rows.sort_values(by='strike', ascending=False, inplace=True)

# Concatenate the sorted DataFrames to combine the "FAILED" and "OK" status rows
sorted_csv_input = pd.concat([failed_rows, ok_rows])

# Now the 'sorted_csv_input' DataFrame will have "FAILED" status rows sorted by 'strike' in descending order,
# and the "OK" status rows sorted by 'strike' in descending order, with "FAILED" ones above "OK" ones.
sorted_csv_input.to_csv('prioritization.csv', index=False)
