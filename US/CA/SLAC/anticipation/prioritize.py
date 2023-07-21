import pandas as pd

# Read the CSV file and use the 'status' column as the sort key
csv_input = pd.read_csv('path_result_plot.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike', 'status','income'])

# Sort the DataFrame for "FAILED" status rows in descending order based on the 'strike' column
failed_rows = csv_input[csv_input['status'] == 'FAILED']
failed_rows.sort_values(by='strike', ascending=False, inplace=True)

# Find the lowest income value and highlight failed_rows with that value
lowest_income_value = failed_rows['income'].min()
def highlight_lowest_income_rows(row):
    # Create a Series of styles with the same length as the row
    styles = ['background-color: yellow' if value == lowest_income_value else '' for value in row]
    return styles

# Use the apply method to apply the highlighting function row-wise to the DataFrame
highlighted_failed_rows = failed_rows.style.apply(highlight_lowest_income_rows, axis=1)
highlighted_failed_rows_html = highlighted_failed_rows.render()

# Save the highlighted DataFrame as an HTML file
with open('highlighted_failed_rows.html', 'w') as f:
    f.write(highlighted_failed_rows_html)

# Sort the DataFrame for "OK" status rows in descending order based on the 'strike' column
ok_rows = csv_input[csv_input['status'] == 'OK']
ok_rows.sort_values(by='strike', ascending=False, inplace=True)

# Concatenate the sorted DataFrames to combine the "FAILED" and "OK" status rows
sorted_csv_input = pd.concat([failed_rows, ok_rows])

# Now the 'sorted_csv_input' DataFrame will have "FAILED" status rows sorted by 'strike' in descending order,
# and the "OK" status rows sorted by 'strike' in descending order, with "FAILED" ones above "OK" ones.
sorted_csv_input.to_csv('prioritization.csv', index=False)