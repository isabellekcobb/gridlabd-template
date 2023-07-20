import pandas as pd

csv_input = pd.read_csv('path_result.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike'])
csv_input['status'] = 'OK'    # set default as OK

# read the strike value 
strike_threshold = 0.1

#load in the income values
income_in=pd.read_csv('merged_results.csv', usecols=['median_all'])
csv_input['income']=income_in

for index, row in csv_input.iterrows():
    if row['strike'] > strike_threshold:
        csv_input.loc[index, "status"] = 'FAILED'

csv_input.to_csv('path_result_plot.csv', index=False)
