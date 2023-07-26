import pandas as pd
import gridlabd

# Define a function to process the data after the simulation is completed
def process_data():
    services = []

    # Use 'meter' as the type argument to get objects of the 'meter' class
    objects = gridlabd.get('meter')

    for index, value in objects.items():
        parent_obj = gridlabd.get_value(value, 'parent')
        if gridlabd.get_class(parent_obj) == 'pole':
            critical_level = gridlabd.get_value(value, 'service_level')
            services.append(critical_level)
        else:
            services.append(0)

    # Convert the 'services' list to a DataFrame and save it to a CSV file
    df = pd.DataFrame({'service level': services})
    df.to_csv('service_level.csv', index=False)

# Load the GridLAB-D model (network.glm) and register the process_data() function to run at the end of the simulation
gridlabd.command('network.glm')
gridlabd.at("end", process_data)

# Start the GridLAB-D simulation
gridlabd.start()
