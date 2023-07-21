import pandas as pd

# Read the CSV file into a DataFrame
csv_input = pd.read_csv('path_result_plot.csv')

# Filter rows with 'FAILED' status
failed_rows = csv_input[csv_input['status'] == 'FAILED']

# Save the filtered rows to a new CSV file
failed_rows.to_csv('failed_results.csv', index=False)
