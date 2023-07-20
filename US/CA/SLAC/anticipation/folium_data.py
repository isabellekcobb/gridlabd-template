import pandas as pd

csv_input = pd.read_csv('path_result.csv', usecols=['position', 'latitude', 'longitude', 'linesag', 'linesway', 'contact', 'strike', 'income'])
csv_input['status'] = 'OK'    # set default as OK

# read the strike value 
strike_threshold = 0.1

#read the income values
income_in=pd.read_csv('merged_results.csv', usecols=['median_all'])

for index, row in csv_input.iterrows():
    if row['strike'] > strike_threshold:
        csv_input.loc[index, "status"] = 'FAILED'
    
    # load the income column with the generated data based on pole location
    csv_input.loc[index, "income"] = income_in[index]

csv_input.to_csv('path_result_plot.csv', index=False)
