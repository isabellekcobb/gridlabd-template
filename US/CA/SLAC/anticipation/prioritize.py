import pandas as pd

# Read the CSV file into a DataFrame
csv_input = pd.read_csv('path_result_plot.csv')

# Filter rows with 'FAILED' status
failed_rows = csv_input[csv_input['status'] == 'FAILED']

# Sort the failed_rows based on 'strike' column in descending order
failed_rows_sorted = failed_rows.sort_values(by='strike', ascending=False)

# Save the filtered rows to a new CSV file
failed_rows_sorted.to_csv('failed_results_sorted.csv', index=False)
